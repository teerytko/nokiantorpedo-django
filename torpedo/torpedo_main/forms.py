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
        if value and not self.VALID_PHONE_NUMBER.match(value):
            raise forms.ValidationError(self.default_error_messages['invalid'])


def create_labeled_field(field, label, *args, **kwargs):
        widget = forms.TextInput(attrs={'class':'form-control',
                                        'placeholder':  'Anna %s' % label})
        kwargs['label'] = label
        kwargs['widget'] = widget
        return field(*args, **kwargs)


class UserProfileForm(forms.Form):
    firstname = create_labeled_field(forms.CharField, 'Etunimi', required=False)
    lastname = create_labeled_field(forms.CharField, 'Sukunimi', required=False)
    email = create_labeled_field(forms.EmailField, 'Email', required=False)
    phonenumber = create_labeled_field(FIPhoneNumberField, 'Puhelinnumero', required=False)
    #userimage = create_labeled_field(forms.ImageField, 'Kuva', required=False)
