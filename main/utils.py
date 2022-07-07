from .models import *


class DataMixin:

    def get_rub_data(self, **kwargs):
        context = kwargs
        rubs = Rub.objects.all()
        context['rubs'] = rubs
        if 'rub_selected' not in context:
            context['rub_selected'] = 0
        return context