from django.shortcuts import render
from django.views.generic import ListView
from main.models import *
from .utils import *
# Create your views here.W


class Main(DataMixin, ListView,):
    model = VideoCard
    
    template_name = 'main/index.html'
    context_object_name = 'videocard'
    


    def get_context_data(self,*,objects_list=None,**kwargs): 
        context = super().get_context_data(**kwargs) 
        c_def = self.get_rub_data()

        return dict(list(context.items()) + list(c_def.items()))
    #def get_queryset(self):
    #    return super().get_queryset().filter(user_id=self.request.user.id)

class RubList(ListView):
    model = VideoCard