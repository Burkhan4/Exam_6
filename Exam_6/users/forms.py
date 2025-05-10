from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField, ModelForm
from .models import CustomUser
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    email = EmailField()

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


User = get_user_model()


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']