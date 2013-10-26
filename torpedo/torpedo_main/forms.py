#!/usr/bin/python
'''
Created on 25.8.2012

@author: teerytko
'''

import re
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from torpedo_main.models import Section
from django.utils.translation import gettext_lazy as _

from registration.forms import RegistrationFormUniqueEmail

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


class MemberProfileForm(forms.Form):
    name = _('Membership details')
    action = '/memberdlg'
    payments = create_labeled_field(forms.CharField, _('Seasonfee'), required=False)
    memberof = create_labeled_field(forms.ModelMultipleChoiceField, _('Sections'), 
                                    queryset=Section.objects.all(),
                                    required=False)

