from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView ,CreateView
from main.models import *
from django.contrib.auth.views import LoginView
from .utils import *
from .form import *
from cart.cart import Cart


class Main(DataMixin, ListView):

    model = VideoCard
    
    template_name = 'main/index.html'
    context_object_name = 'videocard'
    

    def get_context_data(self,*,objects_list=None,**kwargs): 
        context = super().get_context_data(**kwargs) 
        c_def = self.get_rub_data()

        
        return dict(list(context.items()) + list(c_def.items()))
    #    return context
    #def get_queryset(self):
    #    return super().get_queryset().filter(user_id=self.request.user.id)

class RubList(ListView,DataMixin):
    model = VideoCard

    template_name = 'main/index.html'
    context_object_name = 'videocard'

    def get_queryset(self):
        return VideoCard.objects.filter(rub_key__slug_field=self.kwargs['cat_slug'])
    
    def get_context_data(self,*,objects_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
       
#        c = Rub.objects.get(slug_field = self.kwargs['cat_slug'])
        c_def = self.get_rub_data(rub_selected = context['videocard'][0].rub_key)
        return dict(list(context.items()) + list(c_def.items()))
    #    return context
        
class ShowCard(DetailView,DataMixin):
    model = VideoCard
    context_object_name = 'card'
    template_name = 'main/card.html'
    slug_url_kwarg = 'card_slug'
    
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_rub_data()
        return dict(list(context.items()) + list(c_def.items()))

class LoginUser(LoginView,DataMixin):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_rub_data(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('main')    

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_rub_data(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


def about(request):
        return render(request, 'main/about', {'menu': menu})
