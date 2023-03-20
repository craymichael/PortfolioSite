# ==============================================================================
# Portfolio Website
# Copyright (C) 2019  Zachariah Carmichael
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
# ==============================================================================
import urllib.parse
import urllib.request
import json

from django import forms

from PortfolioSite import settings

VERIFY_URL = 'https://www.google.com/recaptcha/api/siteverify'


class ContactForm(forms.Form):
    # https://en.wikipedia.org/wiki/Hubert_Blaine_Wolfeschlegelsteinhausenbergerdorff,_Sr.
    contact_name = forms.CharField(max_length=666, required=True)
    contact_email = forms.EmailField(required=True)
    message = forms.CharField(max_length=10000, required=True,
                              widget=forms.Textarea)

    def __init__(self, *args, request=None, **kwargs):
        if request is None:
            raise ValueError('Missing required kwarg `request` (cannot be '
                             '`None`)')
        self.request = request
        super(ContactForm, self).__init__(*args, **kwargs)

    def clean(self):
        ca = self.request.POST['g-recaptcha-response']
        params = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': ca,
        }
        data = urllib.parse.urlencode(params).encode()
        req = urllib.request.Request(VERIFY_URL, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())

        status = result.get('success', False)
        if not status:
            raise forms.ValidationError(
                'Invalid reCAPTCHA. Please try again.',
                code='invalid',
            )
        return super(ContactForm, self).clean()
