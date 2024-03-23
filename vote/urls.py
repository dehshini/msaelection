from django.contrib import admin
from django.urls import path
from vote import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login', views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('register', views.RegisterView, name='register'),
    path('vote', views.VoteView, name='vote'),
    path('votepoll', views.Votepoll, name='votepoll'),
    path('votes', views.VotesView, name='votes'),
    path('voted', views.VotedView, name='voted'),
    path('results', views.ResultsView, name='results'),
    path('instructions', views.InstructionsView, name='instructions'),
    path('about', views.AboutView, name='about'),
    path('upload_users', views.Upload_users, name='upload_users'),
    path('password_reset', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name="password_reset"),
    path('password_reset_sent', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name="password_reset_confirm"),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "UDSMSA EC Admin"
admin.site.site_title = "EC Admin Portal"
admin.site.index_title = "Welcome"