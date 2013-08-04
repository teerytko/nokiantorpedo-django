#!/usr/bin/python
# -*- coding: utf8 -*-
'''
Created on 18.7.2012
@author: teerytko
'''
from django.utils.datastructures import SortedDict

class MenuItem(object):
    def __init__(self, name, href, access='public'):
        self.name = name
        self.href = href
        self.access = access
        self.children = SortedDict()

class RootMenu(MenuItem):
    def __init__(self):
        super(RootMenu, self).__init__('root', '/')
        self.active = ''

    def sorteddict(self):
        return self.children

    def __getattr__(self, name):
        return getattr(self.children, name)


mymenu = RootMenu()
mymenu.children['home'] = MenuItem(name='Koti', href='/')
mymenu.children['floorball'] = MenuItem(name='Salibandy', href='/floorball')
mymenu.children['endurance'] = MenuItem(name='Kestävyysurheilu', href='/endurance')
#mymenu.children['calendar'] = MenuItem(name='Kalenteri', href='/calendar', access='private')
mymenu.children['association'] = MenuItem(**{'name': 'Yhdistys', 'href': '/association'})
mymenu.children['forum'] = MenuItem(**{'name': 'Forum', 'href': '/forum'})


def get_menu():
    return mymenu