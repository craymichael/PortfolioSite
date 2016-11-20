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
from django.core.exceptions import ImproperlyConfigured
from django.views import generic


class BaseTemplateView(generic.TemplateView):
    active = None

    def render_to_response(self, context, **response_kwargs):
        """
        Returns a response, using the `response_class` for this
        view, with a template rendered with the given context.

        If any keyword arguments are provided, they will be
        passed to the constructor of the response class.
        """
        if self.active is None:
            raise ImproperlyConfigured("BaseTemplateView requires either a definition of 'active'")
        return super(BaseTemplateView, self).render_to_response(context, **response_kwargs)

    def get_context_data(self, **kwargs):
        context = super(BaseTemplateView, self).get_context_data(**kwargs)
        context['active'] = self.active
        return context


class IndexView(BaseTemplateView):
    template_name = 'portfolio/index.html'
    active = 'index'


class PortfolioView(BaseTemplateView):
    template_name = 'portfolio/portfolio.html'
    active = 'portfolio'


class ProjectsView(BaseTemplateView):
    template_name = 'portfolio/projects.html'
    active = 'projects'


class ContactView(BaseTemplateView):
    template_name = 'portfolio/contact.html'
    active = 'contact'
