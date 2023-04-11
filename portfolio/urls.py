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
from django.urls import include, re_path

from . import views

app_name = 'portfolio'

project_patterns = [
    re_path(r'^$', views.ProjectsView.as_view(), name='projects'),
    # re_path(r'^/portfolio-site/$', views.PortfolioSiteProjectView.as_view(), name='portfolio-site'),
    # re_path(r'^/st-huberts-isle/$', views.StHubertProjectView.as_view(), name='st-hubert'),
]

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view(), name='index'),
    re_path(r'^portfolio$', views.PortfolioView.as_view(), name='portfolio'),
    re_path(r'^projects', include(project_patterns)),
    re_path(r'^blog$', views.BlogView.as_view(), name='blog'),
    re_path(r'^contact$', views.contact, name='contact'),
    re_path(r'^[cC][vV]$', views.cv_view, name='cv'),
]
