from django.shortcuts import render
from django.views.generic import ListView, DetailView
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