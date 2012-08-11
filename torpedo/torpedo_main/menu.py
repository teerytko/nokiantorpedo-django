'''
Created on 18.7.2012

@author: teerytko
'''
from django.utils.datastructures import SortedDict

mainmenu = SortedDict()
mainmenu['home'] = {'name': 'Koti', 'href': '/'}
# mainmenu['team'] = {'name': 'Joukkue', 'href': '/team'}
mainmenu['forum'] = {'name': 'Forum', 'href': '/forum'}
mainmenu['association'] = {'name': 'Yhdistys', 'href': '/association'}


class Menu(object):
    def __init__(self, menu):
        self.mainmenu = menu.copy()
        self.active = ''

    def sorteddict(self):
        return self.mainmenu

    def __getattr__(self, name):
        return getattr(self.mainmenu, name)


mymenu = Menu(mainmenu)

def get_menu():
    return mymenu