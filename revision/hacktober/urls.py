from django.conf.urls import url
from hacktober import views
urlpatterns = [
    url(r'^$', views.index, name='index')
]
