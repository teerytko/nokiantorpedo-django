'''
Created on 14.11.2012

@author: tsrytkon
'''

from django import template
register = template.Library()

@register.filter('can_see')
def can_see(menuitem, user):
    if menuitem.access is 'admin':
        if user.is_staff:
            return True
        else:
            return False
    elif menuitem.access is 'private':
        if user.is_authenticated():
            return True
        else:
            return False
    return True
