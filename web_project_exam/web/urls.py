from django.urls import path
from django.contrib.auth import views as auth_views
from web_project_exam.web import views

urlpatterns = [
    path("", views.base, name="home page"),
    path("user_login", views.user_login, name="login page"),
    path("sign up", views.sign_up, name="sign up page"),
    path("profile page", views.profile_page, name="profile page"),
    path("about japan", views.about_japan, name="about japan"),
    path("about japan with profile", views.about_japan_with_profile, name="about japan with profile"),
    path("japanese culture", views.japanese_culture, name="japanese culture"),
    path("japanese culture with profile", views.japanese_culture_with_profile, name="japanese culture with profile"),
    path("modern japan", views.modern_japan, name="modern japan"),
    path("modern japan with profile", views.modern_japan_with_profile, name="modern japan with profile"),
    path("japanese history", views.japanese_history, name="japanese history"),
    path("japanese history with profile", views.japanese_history_with_profile, name="japanese history with profile"),
    path("emperors", views.emperors_overview, name="emperors"),
    path("shogunates", views.shogunates_overview, name="shogunates"),
    path("samurai", views.samurai_overview, name="samurai"),
    path("ninjas", views.ninjas_overview, name="ninjas"),
    path("profile delete", views.profile_delete, name="profile delete"),
    path("edit profile", views.edit_profile, name="edit profile"),
    path("change password", views.change_password, name="change password"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
