from django.contrib.auth.forms import UserCreationForm
from django import forms
from . import models
from django.db.models.signals import post_save
from django.dispatch import receiver


GENDER = (("Male", "Male"), ("Female", "Female"))


class CustomRegistrationForm(UserCreationForm):
    name = forms.CharField(required=True)
    surname = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.ChoiceField(choices=GENDER, required=True)
    experience = forms.IntegerField(required=True)
    telegram = forms.CharField(required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "name",
            "surname",
            "gender",
            "phone",
            "age",
            "experience",
            "telegram",
        )

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


@receiver(post_save, sender=models.CustomUser)
def set_exp(sender, instance, created, **kwargs):
    if created:
        print("Сигнал есть.")
        exp = instance.experience
        if exp < 1:
            instance.club = "Vagabond"
        elif 1 <= exp <= 2:
            instance.club = "Beginner"
        elif 2 <= exp <= 3:
            instance.club = "Simpleton"
        elif 3 <= exp <= 5:
            instance.club = "Knight"
        elif exp > 5:
            instance.club = "Duke"
