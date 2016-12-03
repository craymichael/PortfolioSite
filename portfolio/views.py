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
from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect, render, reverse
from django.template import Context
from django.template.loader import get_template
from django.views import generic

import json

from . import config
from .forms import ContactForm


class BaseTemplateView(generic.TemplateView):
    active = None
    context = {}

    def render_to_response(self, context, **response_kwargs):
        """
        Returns a response, using the `response_class` for this
        view, with a template rendered with the given context.

        If any keyword arguments are provided, they will be
        passed to the constructor of the response class.
        """
        if self.active is None:
            raise ImproperlyConfigured('BaseTemplateView requires either a definition of "active"')
        return super(BaseTemplateView, self).render_to_response(context, **response_kwargs)

    def get_context_data(self, **kwargs):
        context = super(BaseTemplateView, self).get_context_data(**kwargs)
        context['active'] = self.active
        context.update(self.context)
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


def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            # Gather form information
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('message', '')

            # Render email template with name and message
            # Email not included; reply to message to view sender's actual email (stored in headers)
            template = get_template('portfolio/common/contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content
            })
            content = template.render(context)

            # Create and send email message
            email = EmailMessage(subject='[DJANGO] Portfolio Inquiry',
                                 body=content,
                                 to=[config.TO_EMAIL],
                                 reply_to=[contact_email])
            email.send()

            # Add success message in browser storage
            messages.success(request, 'Thanks for the inquiry! I\'ll get back to you as soon as I can.')

            return redirect(reverse('portfolio:contact'))
    else:
        form = form_class()

    return render(request, 'portfolio/contact.html', context={'form': form, 'active': 'contact'})
