from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


class CreateUser(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/sinin.html'
    success_url = reverse_lazy('login')

