from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'$', views.index, name='index'),
    url(r'^(?P<link_id>\w+)$', views.redirect_full_link, name='test'),
    #url(r'^test$', views.redirect_full_link, name='test'),
]
