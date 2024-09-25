from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('handbook/', views.handbook, name='handbook'),
    path('advice/', views.advice, name='advice'),
    path('players/', views.player_list, name='players'),
    path("accounts/register/", views.register, name="register"),
    path('history/', views.history, name='history'),
    path('rules/', views.rules, name='rules'),
    path('strategies/', views.strategies, name='strategies'),
    path('tournaments/', views.tournaments, name='tournaments'),
    path('top_players/', views.top_players, name='top_players'),
    path('combinations/', views.combinations, name='combinations'),
    path('player/<int:pk>/', views.player_profile, name='player_profile'),
    # Добавьте <int:tournament_id> для передачи идентификатора турнира
    path('tournament/register/<int:tournament_id>/', views.register_tournament, name='register_tournament'),
    path('tournament/<int:id>/', views.tournament_detail, name='tournament_detail'),

    # URL для детальной информации о турнире

    path('top_players/magnus-carlsen', views.magnus_carlsen, name='magnus_carlsen'),
    path('top_players/gukesh-dommaraju/', views.gukesh_dommaraju, name='gukesh-dommaraju'),
    path('top_players/fabiano-caruana/', views.fabiano_caruana, name='fabiano_caruana'),
    path('top_players/anish-giri/', views.anish_giri, name='anish_giri'),
    path('top_players/ian-nepomniachtchi/', views.ian_nepomniachtchi, name='ian_nepomniachtchi'),
    path('top_players/hikaru-nakamura/', views.hikaru_nakamura, name='hikaru_nakamura'),
    path('top_players/wesley-so/', views.wesley_so, name='wesley_so'),
    path('top_players/maxime-vachier-lagrave/', views.maxime_vachier_lagrave, name='maxime_vachier_lagrave'),
    path('top_players/levon-aronian/', views.levon_aronian, name='levon_aronian'),
]
