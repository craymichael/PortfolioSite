from django.conf.urls import url

from . import views

app_name = 'portfolio'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^portfolio/$', views.PortfolioView.as_view(), {'active': 'portfolio'}, name='portfolio'),
    url(r'^projects/$', views.ProjectsView.as_view(), {'active': 'projects'}, name='projects'),
    url(r'^contact/$', views.ContactView.as_view(), {'active': 'contact'}, name='contact'),
]
