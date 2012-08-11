'''
Created on 11.8.2012

@author: teerytko
'''



from torpedo_main.menu import mainmenu
mainmenu['statistics'] =     {'name': 'Statistiikat',
     'href': '/statistics',
     'children': [
        {'name': 'Pelaajat', 'href': '/statistics/players'},
        {'name': 'Ottelut', 'href': '/statistics/games'},
        ]
    }
