from django.test import TestCase

from authenticator.forms import UserCreationForm
from authenticator.models import User


class UserCreationFormTest(TestCase):
    """Unit tests for UserCreationForm"""

    def test_valid_data(self):
        """Test successful form submission with valid data"""
        data = {
            "email": "test@example.com",
            "password1": "strongpassword",
            "password2": "strongpassword",
        }
        form = UserCreationForm(data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(user.email, data["email"])

    def test_invalid_email(self):
        """Test form validation with an invalid email"""
        data = {
            "email": "invalid_email",
            "password1": "strongpassword",
            "password2": "strongpassword",
        }
        form = UserCreationForm(data)
        self.assertFalse(form.is_valid())

    def test_password_mismatch(self):
        """Test form validation with mismatched passwords"""
        data = {
            "email": "test@example.com",
            "password1": "strongpassword",
            "password2": "differentpassword",
        }
        form = UserCreationForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["password2"], ["The two password fields didn't match."]
        )

    def test_save_creates_user(self):
        """Test that save method creates a user and sets password"""
        data = {
            "email": "test@example.com",
            "password1": "strongpassword",
            "password2": "strongpassword",
        }
        form = UserCreationForm(data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertIsInstance(user, User)
        self.assertTrue(user.check_password(data["password1"]))

    def test_save_commit_false(self):
        """Test that save method with commit=False doesn't save the user"""
        data = {
            "email": "test@example.com",
            "password1": "strongpassword",
            "password2": "strongpassword",
        }
        form = UserCreationForm(data)
        user = form.save(commit=False)

        assert form.is_valid()
        assert hasattr(user, "pk")  # Check if user object has a primary key
        self.assertIsInstance(user, User)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(email=data["email"])
