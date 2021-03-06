'''
Created on 14.11.2012

@author: tsrytkon
'''

from django import template
register = template.Library()
from torpedo_main.menu import get_menu
from django import template

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

@register.tag(name='get_menu')
def get_menu(parser, token):
    return DefaultMenuNode()

class DefaultMenuNode(template.Node):
    def __init__(self, format_string):
        pass
    def render(self, context):
        return get_menu()