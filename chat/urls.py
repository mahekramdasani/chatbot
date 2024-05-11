from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/', views.user_registration, name='user-registration'),
    path('login/', views.user_login, name='user-login'),
    path('chat/', views.chat_interaction, name='chat'),
    path('balance/', views.token_balance, name='token-balance'),
    path('logout/',views.user_logout,name='user-logout')
]
