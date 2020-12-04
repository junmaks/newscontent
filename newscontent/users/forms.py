from django.contrib.auth.forms import ReadOnlyPasswordHashField, AuthenticationForm
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Account


class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class': 'form-control', }))
    password2 = forms.CharField(label='Повторно введите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', }))

    class Meta:
        model = Account
        fields = ('username', 'email',)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = Account.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Пользователь с таким логином уже зарегистрирован")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = Account.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Данный email зарегистрирован")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self):
        user = super(RegisterForm, self).save()
        user.set_password(self.cleaned_data["password2"])
        user.save()
        return user


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username', 'email', )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ('email', 'password', )

    def clean_password(self):
        return self.initial["password"]


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', }))
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class': 'form-control', }))

