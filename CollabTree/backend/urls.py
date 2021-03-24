from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name = "index"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('signup/', views.sign_up, name = 'signup'),
]