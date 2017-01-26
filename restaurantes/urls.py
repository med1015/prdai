from django.conf.urls import url, include

from restaurantes import views


urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^test/$', views.test, name='test'),
  url(r'^add_rest/',views.add_rest, name='add_rest'),
 ] 
