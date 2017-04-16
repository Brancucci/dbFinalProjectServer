from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^search/city$', views.search_city, name='search_city'),
    url(r'^search/country$', views.search_country, name='search_country'),
    url(r'search/city&country', views.search_city_country, name='search_city_country'),
]
