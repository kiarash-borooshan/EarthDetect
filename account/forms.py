from django.contrib.auth import authenticate

from .models import Account
from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ("email", "username", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError(f" ایمیل {account} قبلا استفاده شده است.")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError(f" نام کاربری {account} قبلا استفاده شده است.")


class LoginForm(forms.ModelForm):
    password = forms.CharField(label="Password",
                               widget=forms.TextInput(
                                   attrs={"class": "form-control"}
                               ))
    email = forms.CharField(label="email",
                            widget=forms.EmailInput(
                                attrs={"class": "form-control"}
                            ))

    class Meta:
        model = Account
        fields = ("email", "password")

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data["email"]
            password = self.cleaned_data["password"]
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("ایمیل یا رمز عبور را تصحیح کنید ")


class AccountUpdateForm(forms.ModelForm):
    profile_image = forms.ImageField(widget=forms.FileInput)

    class Meta:
        model = Account
        fields = ('username', 'email', 'profile_image')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
        except Account.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" is already in use.' % account)

    def save(self, commit=True):
        account = super(AccountUpdateForm, self).save(commit=False)
        account.username = self.cleaned_data['username']
        account.email = self.cleaned_data['email'].lower()
        account.profile_image = self.cleaned_data['profile_image']
        if commit:
            account.save()
        return account
