from django.shortcuts import render
from django.views.generic import ListView
from main.models import *
# Create your views here.


class Main(ListView):
    model = VideoCard
    
    template_name = 'main/index.html'
    context_object_name = 'videocard'
    
    def get_context_data(self,*,objects_list=None,**kwargs): 
        context = super().get_context_data(**kwargs)
        return context
    #def get_queryset(self):
    #    return super().get_queryset().filter(user_id=self.request.user.id)
    
    