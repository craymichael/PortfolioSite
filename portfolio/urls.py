# ======================================================================================================================
# Portfolio Website
# Copyright (C) 2016  Zachariah Carmichael
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program.  If not, see
# <http://www.gnu.org/licenses/>.
# ======================================================================================================================
from django.conf.urls import include, url

from . import views

app_name = 'portfolio'

project_patterns = [
    url(r'^$', views.ProjectsView.as_view(), name='projects'),
    # url(r'^/portfolio-site/$', views.PortfolioSiteProjectView.as_view(), name='portfolio-site'),
    # url(r'^/st-huberts-isle/$', views.StHubertProjectView.as_view(), name='st-hubert'),
]

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^portfolio$', views.PortfolioView.as_view(), name='portfolio'),
    url(r'^projects', include(project_patterns)),
    url(r'^contact$', views.contact, name='contact'),
]
