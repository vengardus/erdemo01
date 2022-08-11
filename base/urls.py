from django.urls import path
from base import views

# MIS CUENTAS
from base.views import home_view, login_view

urlpatterns = [
    path('', home_view.main, name='main'),
    path('login/', login_view.login_app, name='login'),
    path('logout/', login_view.logout_app, name='logout'),
    path('account/', login_view.account, name='account'),
    path('register/', login_view.registerUser, name='register'),
    path('about/', login_view.about, name='about'),

]

