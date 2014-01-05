'''
Created on Jan 5, 2014

@author: tsrytkon
'''

from torpedo_main.menu import get_menu

def load_menu(request):
    """Loads the menu for the context for the given request"""
    menu = get_menu()
    menu.active = get_active_menu(menu, request.path)
    return {'torpedo_menu': menu}

def get_active_menu(menu, path):
    prepath = '/' + path.strip('/').split('/')[0]
    if prepath == '/manage':
        return 'manage'
    for key, item in menu.items():
        if item.href == prepath:
            return key
