from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(User):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=14, default='+996')
    age = models.PositiveIntegerField(default=18, validators=[MinValueValidator(10), MaxValueValidator(90)])
    gender = models.CharField(max_length=10, choices=GENDER)
    experience = models.PositiveIntegerField(default=0)
    telegram = models.CharField(max_length=50, default='@')
    club = models.CharField(max_length=100, default='Vagabond')


@receiver(post_save, sender=CustomUser)
def set_exp(sender, instance, created, **kwargs):
    if created:
        print('Сигнал есть.')
        exp = instance.experience
        if exp < 1:
            instance.club = 'Vagabond'
        elif 1 <= exp <= 2:
            instance.club = 'Beginner'
        elif 2 <= exp <= 3:
            instance.club = 'Simpleton'
        elif 3 <= exp <= 5:
            instance.club = 'Knight'
        elif exp > 5:
            instance.club = 'Duke'