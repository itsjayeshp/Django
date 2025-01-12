from datetime import datetime
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView ,LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
# Create your views here.


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)

class LogoutInterfaceView(LogoutView):
    template_name  = 'home/bye.html'
    
class LoginInterfaceView(LoginView):
    template_name = 'home/log.html'

class HomeView(TemplateView):
    template_name = 'home/home.html'
    extra_context = {'today':datetime.today()}

class Authorizedview(LoginRequiredMixin,TemplateView):
    template_name =  'home/authorized.html'
    login_url = '/admin'


