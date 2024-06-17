"""
URL configuration for gestaoacademica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from authenticator.views import LogoutView
from gestaoacademica.views import (
    HomePageView,
    OfertaDisciplinaListView,
    ParticipacaoCreateView,
    AlunoCreateView,
    AlunoDisciplinaListView,
    LoginPageView,
    SeInscreverEmoutraDisciplina,
    EntrarNaListaDeEspera,
    AlunoDisciplinaCancelaInscricao,
    AlunoDisciplinaCancelaListaDeEspera
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", LoginPageView.as_view(), name="accounts_login"),
    path("accounts/logout/", LogoutView.as_view(), name="accounts_logout"),
    path("accounts/register/aluno/", AlunoCreateView.as_view(), name="alunos_create"),
    path("", HomePageView.as_view(), name="home_page"),
    path(
        "disciplinas/",
        OfertaDisciplinaListView.as_view(),
        name="oferta_disciplina_list",
    ),
    path(
        "participacao/create",
        ParticipacaoCreateView.as_view(),
        name="participacao_create",
    ),
    path(
        "disciplinas/outra",
        SeInscreverEmoutraDisciplina.as_view(),
        name="se_inscrever_em_outra_materia",
    ),
    path(
        "disciplinas/listadeespera",
        EntrarNaListaDeEspera.as_view(),
        name="entrar_na_lista_de_espera",
    ),
    path(
        "alunos/disciplinas",
        AlunoDisciplinaListView.as_view(),
        name="aluno_disciplina_list",
    ),
    path(
        "alunos/disciplinas/cancelar",
        AlunoDisciplinaCancelaInscricao.as_view(),
        name="aluno_disciplina_cancelar",
    ),
    path(
        "alunos/disciplinas/cancelarlista",
        AlunoDisciplinaCancelaListaDeEspera.as_view(),
        name="aluno_disciplina_cancelar_lista",
    ),
]
