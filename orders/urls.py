#from django.conf.urls import url
from . import views
from django.urls import include, path

urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path(r'^admin/order/(?P<order_id>\d+)/$', views.admin_order_detail, name='admin_order_detail'),
    path('test/',views.num)
]