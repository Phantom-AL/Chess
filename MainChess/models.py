from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Players(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    rating = models.IntegerField(default=400)
    profile_link = models.URLField(max_length=200, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('player_profile', kwargs={'pk': self.pk})


class Tournament(models.Model):
    name = models.CharField(max_length=255, default="Шахматный Турнир")
    location = models.CharField(max_length=255, default="Лондон, Великобритания")
    date = models.DateField(default="2024-10-10")  # Дата по умолчанию — 10 октября 2024
    current_participants = models.IntegerField(default=0)
    max_participants = models.IntegerField(default=32)
    prize_fund = models.CharField(max_length=255, default="50,000 фунтов")
    prize_description = models.TextField(default="Призовой фонд будет распределён среди победителей турнира.")
    rules_title = models.CharField(max_length=255, default="Швейцарская система в 7 туров")
    rules_description = models.TextField(default="Контроль времени на каждую партию: 90 минут.")
    schedule = models.TextField(default="0")
    additional_info = models.TextField(default="Турнир проводится в Лондонском шахматном клубе.")
    registration_info = models.TextField(default="Регистрация доступна до 1 октября 2024 года.")
    contact_email = models.EmailField(default="info@chesslondon2024.com")
    contact_phone = models.CharField(max_length=20, default="+44 123 456 789")

    def __str__(self):
        return self.name


class ScheduleEvent(models.Model):
    tournament = models.ForeignKey(Tournament, related_name='schedule_events', on_delete=models.CASCADE)
    time = models.TimeField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.tournament.name} - {self.description}"


class TournamentRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Ссылка на пользователя
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)  # Ссылка на турнир

    class Meta:
        unique_together = ('user',
                           'tournament')  # Ограничение уникальности, чтобы один пользователь мог зарегистрироваться только один раз на один турнир

    def __str__(self):
        return f"{self.user.username} - {self.tournament.name}"


class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        unique_together = ('name', 'email')  # Ограничение уникальности для имени и email

    def __str__(self):
        return f"{self.name} ({self.email})"
