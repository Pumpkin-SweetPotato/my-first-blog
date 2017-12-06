from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_shop_list, name='post_shop_list'),
]