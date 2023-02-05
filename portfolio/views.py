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
from __future__ import absolute_import

import os

from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render, reverse
from django.template.loader import get_template
from django.utils.html import escape
from django.views import generic
from django.http import FileResponse, Http404
from django.templatetags.static import static

from django.conf import settings
from .forms import ContactForm


class _BaseTemplateView(generic.TemplateView):
    active = None
    context = {}

    def render_to_response(self, context, **response_kwargs):
        if self.active is None:
            raise ImproperlyConfigured('_BaseTemplateView requires a '
                                       'definition of `active`')
        return super(_BaseTemplateView, self).render_to_response(
            context, **response_kwargs)

    def get_context_data(self, **kwargs):
        context = super(_BaseTemplateView, self).get_context_data(**kwargs)
        context['active'] = self.active
        context.update(self.context)
        return context


class IndexView(_BaseTemplateView):
    template_name = 'portfolio/index.html'
    active = 'index'


class PortfolioView(_BaseTemplateView):
    template_name = 'portfolio/portfolio.html'
    active = 'portfolio'


class ProjectsView(_BaseTemplateView):
    template_name = 'portfolio/projects.html'
    active = 'projects'


class _BaseProjectView(_BaseTemplateView):
    active = 'projects'
    active_project = None

    def render_to_response(self, context, **response_kwargs):
        if self.active_project is None:
            raise ImproperlyConfigured('_BaseTemplateView requires a '
                                       'definition of `active_project`')
        return super(_BaseProjectView, self).render_to_response(
            context, **response_kwargs)

    def get_context_data(self, **kwargs):
        context = super(_BaseProjectView, self).get_context_data(**kwargs)
        context['active_project'] = self.active_project
        context.update(self.context)
        return context


class PortfolioSiteProjectView(_BaseProjectView):
    template_name = 'portfolio/projects/portfolio_site.html'
    active_project = 'portfolio-site'


class StHubertProjectView(_BaseProjectView):
    template_name = 'portfolio/projects/st_hubert.html'
    active_project = 'st-hubert'


def contact(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST, request=request)

        if form.is_valid():
            # Gather form information
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('message', '')

            # Render email template with name and message
            # Email not included; reply to message to view sender's actual email
            # (stored in headers)
            template = get_template('portfolio/common/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content
            }
            content = template.render(context)

            # Create and send email message
            email = EmailMessage(subject='[DJANGO] Portfolio Inquiry',
                                 body=content,
                                 to=[settings.CONTACT_EMAIL],
                                 reply_to=[contact_email])
            email.send()

            # Add success message in browser storage
            messages.success(request, 'Thanks for the inquiry! I will get back '
                                      'to you as soon as I can.')

            return redirect(reverse('portfolio:contact'))
    else:
        form = ContactForm(request=request)

    return render(request, 'portfolio/contact.html',
                  context={'form': form, 'active': 'contact'})


def cv_view(request):
    path = os.path.join(settings.STATIC_ROOT, 'pdf',
                        'Zachariah_Carmichael_CV_20230205.pdf')
    try:
        return FileResponse(open(path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()


CSRF_FAILURE_MSG = '''<h6><b>CSRF verification failed! Request aborted.</b></h6>
<br>
You are seeing this message because this site requires a CSRF cookie when
submitting forms. This cookie is required for security reasons, to ensure that
your browser is not being hijacked by third parties.
<br>
If you have configured your browser to disable cookies, please re-enable them,
at least for this site, or for “same-origin” requests.'''


def csrf_failure(request, reason=''):
    msg = CSRF_FAILURE_MSG
    if reason:
        msg += '<br><b>Reason:</b> ' + escape(reason)
    return render(request, '403.html',
                  context={'message': msg})
