#!/usr/bin/python
'''
Created on 25.8.2012

@author: teerytko
'''

import re
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

from registration.forms import RegistrationFormUniqueEmail
from captcha.fields import CaptchaField

def create_labeled_field(field, label, *args, **kwargs):
        widget_class = kwargs.get('widget', field.widget)
        widget = widget_class(attrs={'class':'form-control',
                                     'placeholder':  _('Give %s') % label})
        kwargs['label'] = label
        kwargs['widget'] = widget
        return field(*args, **kwargs)


class TorpedoRegistrationForm(RegistrationFormUniqueEmail):
    username = create_labeled_field(forms.RegexField, regex=r'^[\w.@+-]+$',
                                max_length=30,
                                label=_("Username"),
                                error_messages={'invalid': _("This value may contain only letters, numbers and @/./+/-/_ characters.")})
    email = create_labeled_field(forms.EmailField, label=_("E-mail"))
    password1 = create_labeled_field(forms.CharField, widget=forms.PasswordInput,
                                label=_("Password"))
    password2 = create_labeled_field(forms.CharField, widget=forms.PasswordInput,
                                label=_("Password (again)"))
    captcha = CaptchaField(label=_("Captcha"))


class TorpedoAuthenticationForm(AuthenticationForm):
    username = create_labeled_field(forms.CharField, label=_("Username"), max_length=30)
    password = create_labeled_field(forms.CharField, label=_("Password"), widget=forms.PasswordInput)



class FIPhoneNumberField(forms.CharField):
    default_error_messages = {
        'invalid': _('Give a valid phonenumber'),
    }
    VALID_PHONE_NUMBER = re.compile('^\d+$')

    def validate(self, value):
        "Check if value consists valid phone number."
        if value and not self.VALID_PHONE_NUMBER.match(value):
            raise forms.ValidationError(self.default_error_messages['invalid'])


class UserProfileForm(forms.Form):
    name = _('Personal details')
    action = '/profiledlg'
    firstname = create_labeled_field(forms.CharField, _('Firstname'), required=False)
    lastname = create_labeled_field(forms.CharField, _('Surname'), required=False)
    email = create_labeled_field(forms.EmailField, _('Email'), required=False)
    phonenumber = create_labeled_field(FIPhoneNumberField, _('Telephone'), required=False)


class UserImageForm(forms.Form):
    name = _('Profile image')
    submit = "Upload"
    action = '/profileimg'
    userimage = create_labeled_field(forms.ImageField, _('Image'), required=False)


class ShortFlatpageForm(forms.Form):
    name = _('Flatpage edit')
    submit = "Save"
    action = '/hmm'
    url = create_labeled_field(forms.RegexField, label=_("URL"), 
                               max_length=100, 
                               regex=r'^[-\w/\.~]+$',
                               help_text = _("Example: '/about/contact/'. Make sure to have leading"
                                             " and trailing slashes."),
                               error_message = _("This value must contain only letters, numbers,"
                                                 " dots, underscores, dashes, slashes or tildes."))
    title = create_labeled_field(forms.CharField, _('Title'), required=False)
    content = create_labeled_field(forms.CharField, _('Content'), 
                                   widget=forms.Textarea,
                                   required=False)

