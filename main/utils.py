from .models import *
from django.db.models import Count

class DataMixin:

    def get_rub_data(self, **kwargs):
        context = kwargs
        rubs = Rub.objects.all()
        context['rubs'] = rubs

        return context