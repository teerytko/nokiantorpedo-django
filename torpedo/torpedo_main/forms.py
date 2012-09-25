'''
Created on 25.8.2012

@author: teerytko
'''

from django import forms
import re

class FIPhoneNumberField(forms.CharField):
    default_error_messages = {
        'invalid': 'Anna validi puhelin numero.',
    }
    VALID_PHONE_NUMBER = re.compile('^\d+$')

    def validate(self, value):
        "Check if value consists valid phone number."
        if not self.VALID_PHONE_NUMBER.match(value):
            raise forms.ValidationError(self.default_error_messages['invalid'])

class UserProfileForm(forms.Form):
    firstname = forms.CharField(required=False)
    lastname = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    phonenumber = FIPhoneNumberField(required=False)
    userimage = forms.ImageField(required=False)
