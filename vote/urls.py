from django.contrib import admin
from django.urls import path, include
from vote import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('register', views.RegisterView, name='register'),
    path('vote', views.VoteView, name='vote'),
    path('votepoll', views.Votepoll, name='votepoll'),
    path('voted', views.VotesView, name='voted'),
    path('results', views.ResultsView, name='results'),
    path('instructions', views.InstructionsView, name='instructions'),
    path('about', views.AboutView, name='about'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
