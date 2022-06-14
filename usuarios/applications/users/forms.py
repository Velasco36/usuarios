from django import forms
from .models import User
from django.contrib.auth import authenticate


class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label= 'Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
            }
        )
    )
    password2 = forms.CharField(
        label= 'Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repit Password',
            }
        )
    )
    class Meta:
        """Meta definition for UserRegisterform."""

        model = User
        fields = (
            'username',
            'email',
            'full_name',
            'last_name',
            'genero'
        )


    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'las contraseñas no son iguales')


class LoginForm(forms.Form):
    username = forms.CharField(
        label= 'username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'style': '{marge: 10px}',
            }
        )
    )

    password = forms.CharField(
        label= 'Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password',
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password= self.cleaned_data['password']

        if not authenticate(username=username, password=password):
            raise forms.ValidationError('Los datos del usuarios no son correcto')

        return self.cleaned_data


class UpdatePasswordForm(forms.Form):
    
    password1 = forms.CharField(
        label= 'Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password actuality',
            }
        )
    )


    password2 = forms.CharField(
        label= 'Password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'new password ',
            }
        )
    )
