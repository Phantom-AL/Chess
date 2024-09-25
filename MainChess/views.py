from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegistrationForm
from .forms import TournamentRegistrationForm
from .models import Players, Tournament, Participant, TournamentRegistration


def index(request):
    return render(request, 'MainChess/main.html')


def handbook(request):
    return render(request, 'MainChess/handbook.html')


def player_list(request):
    players = Players.objects.all()
    return render(request, 'MainChess/players.html', {'players': players})


def player_profile(request, pk):
    player = get_object_or_404(Players, pk=pk)
    return render(request, 'players_profile/player_profile.html', {'player': player})


def edit_player_profile(request, player_id):
    # Получаем игрока по его ID
    player = get_object_or_404(Players, id=player_id)

    if request.method == 'POST':
        # Обновляем данные игрока
        player.name = request.POST.get('name')
        player.bio = request.POST.get('bio')
        player.save()

        # После сохранения перенаправляем обратно на профиль
        return redirect('player_profile', pk=player.id)

    # Если это GET-запрос, просто отобразим страницу профиля
    return render(request, 'players_profile/player_profile.html', {'player': player})


def advice(request):
    return render(request, 'MainChess/advice.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            login(request, user)
            return redirect('home')  # Перенаправление на главную страницу или другую

        else:
            # Добавляем ошибки формы в сообщения
            for error in form.errors.values():
                for e in error:
                    messages.error(request, e)
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def history(request):
    return render(request, 'handbook/history.html')


def rules(request):
    return render(request, 'handbook/rules.html')


def strategies(request):
    return render(request, 'handbook/strategies.html')


def tournaments(request):
    tournaments = Tournament.objects.all()
    return render(request, 'handbook/tournaments.html', {'tournaments': tournaments})


def tournament_detail(request, id):
    # Получаем турнир по идентификатору, если не найдено, возвращаем 404
    tournament = get_object_or_404(Tournament, id=id)
    return render(request, 'tournaments/tournament_detail.html', {'tournament': tournament})


def top_players(request):
    return render(request, 'handbook/top_players.html')


def combinations(request):
    return render(request, 'handbook/combinations.html')


def tournament_london(request):
    return render(request, 'tournaments/london.html')


def tournament_berlin(request):
    return render(request, 'tournaments/berlin.html')


def tournament_paris(request):
    return render(request, 'tournaments/paris.html')


def tournament_rome(request):
    return render(request, 'tournaments/rome.html')


def tournament_madrid(request):
    return render(request, 'tournaments/madrid.html')


def tournament_warsaw(request):
    return render(request, 'tournaments/warsaw.html')


def magnus_carlsen(request):
    return render(request, 'players_biography/magnus_carlsen.html')


# Гукеш Доммараджу
def gukesh_dommaraju(request):
    return render(request, 'players_biography/gukesh_dommaraju.html')


# Страница Фабиано Каруаны
def fabiano_caruana(request):
    return render(request, 'players_biography/fabiano_caruana.html')


# Страница Аниша Гири
def anish_giri(request):
    return render(request, 'players_biography/anish_giri.html')


# Страница Яна Непомнящего
def ian_nepomniachtchi(request):
    return render(request, 'players_biography/ian_nepomniachtchi.html')


# Страница Хикару Накамуры
def hikaru_nakamura(request):
    return render(request, 'players_biography/hikaru_nakamura.html')


# Страница Уэсли Со
def wesley_so(request):
    return render(request, 'players_biography/wesley_so.html')


# Страница Максима Вашье-Лаграва
def maxime_vachier_lagrave(request):
    return render(request, 'players_biography/maxime_vachier_lagrave.html')


# Страница Левона Ароняна
def levon_aronian(request):
    return render(request, 'players_biography/levon_aronian.html')


@login_required  # Убедитесь, что только авторизованные пользователи могут регистрироваться
def register_tournament(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)

    if request.method == 'POST':
        form = TournamentRegistrationForm(request.POST)
        if form.is_valid():
            # Проверяем, не зарегистрирован ли пользователь на этот турнир
            if TournamentRegistration.objects.filter(user=request.user, tournament=tournament).exists():
                messages.error(request, 'Вы уже зарегистрированы на этот турнир.')
                return redirect('tournaments')

            # Логика для регистрации пользователя
            if tournament.current_participants < tournament.max_participants:
                # Регистрируем пользователя на турнир
                TournamentRegistration.objects.create(user=request.user, tournament=tournament)

                tournament.current_participants += 1
                tournament.save()  # Сохраняем обновленное количество участников
                messages.success(request, 'Вы успешно зарегистрировались на турнир!')
            else:
                messages.error(request,
                               'К сожалению, регистрация закрыта. Достигнуто максимальное количество участников.')

            return redirect('tournaments')  # Перенаправляем на страницу со списком турниров
    else:
        form = TournamentRegistrationForm()

    return render(request, 'register_tournament/register.html', {'form': form, 'tournament': tournament})


def some_view(request):
    return render(request, 'MainChess/base.html', {'user': request.user})
