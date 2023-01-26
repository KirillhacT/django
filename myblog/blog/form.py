from django import forms
from django.contrib.auth.models import User

from .models import Comments, PostOn
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("name", "email", "text_comments")


# class AddPostForm(forms.ModelForm):
#     class Meta:
#         model = PostOn
#         fields = ("__all__")




class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Потдверждения пароля", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', "email", "password1", "password2")

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', "email", "password1", "password2")