
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('authorized/', views.Authorizedview.as_view(), name='authorized'),
    path('log/',views.LoginInterfaceView.as_view(), name='notes.login'),
    path('bye/' , views.LogoutInterfaceView.as_view(), name="notes.logout"),
    path('signup/', views.SignupView.as_view(), name='notes.signup'),
]
