from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import views as auth_views

from authenticator.forms import UserCreationForm
from authenticator.models import User
from gestaoacademica.models import Aluno, OfertaDisciplina, Participacao, Turma, Disciplina, ListaDeEspera
from gestaoacademica.forms import AlunoForm

from django.views.generic.base import ContextMixin


class CommonContextMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_creation_form"] = UserCreationForm
        return context


class LoginPageView(auth_views.LoginView, CommonContextMixin):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class HomePageView(LoginRequiredMixin, CommonContextMixin, TemplateView):
    model = Aluno
    login_url = "/accounts/login"
    template_name = "general/home.html"


class AlunoCreateView(CommonContextMixin, CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = "alunos/create.html"
    success_url = reverse_lazy("home_page")

    def post(self, request, *args, **kwargs):
        user_email = request.POST.get("email")
        user_password = request.POST.get("password1")
        user = User.objects.create_user(user_email, user_password)

        aluno_nome = request.POST.get("nome")
        aluno_sobrenome = request.POST.get("sobrenome")
        aluno_prontuario = request.POST.get("prontuario")
        Aluno.objects.create(
            user=user,
            nome=aluno_nome,
            sobrenome=aluno_sobrenome,
            prontuario=aluno_prontuario,
        )
        return HttpResponseRedirect(self.success_url)


class OfertaDisciplinaListView(LoginRequiredMixin, CommonContextMixin, ListView):
    login_url = "/accounts/login"
    model = OfertaDisciplina
    template_name = "disciplinas/list.html"
    queryset = OfertaDisciplina.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        aluno = Aluno.objects.filter(user=self.request.user).first()
        diciplinasInscritas = Participacao.objects.filter(aluno=aluno)
        context["aluno"] = aluno
        context["diciplinasInscritas"] = [
            disciplina.ofertaDisciplina for disciplina in diciplinasInscritas
        ]
        context["len_diciplinasInscritas"] = len(context["diciplinasInscritas"])
        return context


class ParticipacaoCreateView(LoginRequiredMixin, CommonContextMixin, CreateView):
    login_url = "/accounts/login"
    model = Participacao
    fields = ["aluno, ofertaDisciplina"]
    template_name = "disciplinas/list.html"
    success_url = reverse_lazy("home_page")
    failed_url = reverse_lazy("oferta_disciplina_list")

    def post(self, request, *args, **kwargs):
        oferta_ids_list = request.POST.getlist("oferta-disciplina")
        aluno = Aluno.objects.filter(user=self.request.user).first()
        dia_horarios = []
        materias_com_pendencia = []

        if len(oferta_ids_list) > 3:
            messages.error(request, "Créditos excedidos, máximo 3")
            return HttpResponseRedirect(self.failed_url)

        for oferta_id in oferta_ids_list:
            if Participacao.objects.filter(aluno=aluno).count() >= 3:
                messages.error(request, "Créditos excedidos, máximo 3")
                return HttpResponseRedirect(self.failed_url)

            oferta_disciplina = OfertaDisciplina.objects.filter(pk=oferta_id).first()
            oferta_dia_horario = (
                f"{oferta_disciplina.diaDaSemana}-{oferta_disciplina.horarioInicio}"
            )
            if oferta_dia_horario not in dia_horarios:
                dia_horarios.append(oferta_dia_horario)
            else:
                messages.error(request, "Há conflito de horários")
                return HttpResponseRedirect(self.failed_url)

            if (
                oferta_disciplina.sala.capacidade
                == oferta_disciplina.turma.aluno.count()
            ):
                materias_com_pendencia.append(f"{str(oferta_disciplina)}")
                continue

            turma = Turma.objects.filter(pk=oferta_disciplina.turma.id).first()
            turma.aluno.add(aluno)
            turma.save()

            participacao = Participacao(aluno=aluno, ofertaDisciplina=oferta_disciplina)
            participacao.save()
            
        if len(materias_com_pendencia) >0:
            request.session['test'] = materias_com_pendencia
            return HttpResponseRedirect(self.failed_url)
            
        messages.success(request, "Inscrição feita com sucesso")
        return HttpResponseRedirect(self.success_url)

class SeInscreverEmoutraDisciplina(LoginRequiredMixin, CommonContextMixin, ListView):
    def post(self, request, *args, **kwargs):
        oferta_ids_list = request.POST.getlist("disciplina-pendente")[0]
        temp = request.session['test'][:]
        temp.remove(oferta_ids_list)
        request.session['test'] = temp
        return HttpResponseRedirect(reverse_lazy("oferta_disciplina_list"))
    
class EntrarNaListaDeEspera(LoginRequiredMixin, CommonContextMixin, ListView):
    def post(self, request, *args, **kwargs):
        oferta_ids_list = request.POST.getlist("disciplina-pendente")[0]
        temp = request.session['test'][:]
        temp.remove(oferta_ids_list)
        request.session['test'] = temp
        namedisciplina = oferta_ids_list.split(" (")[0]
        print(namedisciplina)
        disciplina = Disciplina.objects.filter(nome=namedisciplina)[0]
        print(disciplina)
        ofertaDisciplina = OfertaDisciplina.objects.filter(disciplina=disciplina)[0]
        aluno = Aluno.objects.filter(user=self.request.user).first()
        if ListaDeEspera.objects.filter(ofertaDisciplina=ofertaDisciplina).exists():
            listaDeEspera =  ListaDeEspera.objects.filter(ofertaDisciplina=ofertaDisciplina)[0]
            listaDeEspera.aluno.add(aluno)
        else:
            listaDeEspera = ListaDeEspera(ofertaDisciplina=ofertaDisciplina)
            listaDeEspera.save()
            listaDeEspera.aluno.add(aluno)
        
        if 'lista_de_espera' in request.session:
            request.session['lista_de_espera'].append(str(ofertaDisciplina))
        else:
            request.session['lista_de_espera'] = [str(ofertaDisciplina)]
        
        
        messages.success(request, "Aluno inserido na lista de espera!")
        return HttpResponseRedirect(reverse_lazy("oferta_disciplina_list"))
    

class AlunoDisciplinaListView(LoginRequiredMixin, CommonContextMixin, ListView):
    login_url = "/accounts/login"
    model = OfertaDisciplina
    template_name = "alunos/list.html"
    queryset = Participacao.objects.filter()

    def get_queryset(self):
        user = self.request.user
        aluno = Aluno.objects.filter(user=user).first()
        participacoes = Participacao.objects.filter(aluno=aluno)
        ofertas_disciplina = []
        for participacao in participacoes:
            if participacao.ofertaDisciplina not in ofertas_disciplina:
                ofertas_disciplina.append(participacao.ofertaDisciplina)
        return ofertas_disciplina
