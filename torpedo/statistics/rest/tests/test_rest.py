"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import unittest
import json
from django_webtest import WebTest


#class SimpleTest(TestCase):
#    def test_basic_addition(self):
#        """
#        Tests that 1 + 1 always equals 2.
#        """
#        self.assertEqual(1 + 1, 2)

class TestGameRest(WebTest):
    fixtures = ['users']

    def test_game_list_on_empty_data(self):
        res = self.app.get('/statistics/rest/game')
        self.assertEquals(json.loads(res.body), [])

    def test_game_dlist_on_empty_data(self):
        res = self.app.get('/statistics/rest/game')
        self.assertEquals(json.loads(res.body),
                          {"aaData": [], "iTotalRecords": 0,
                           "sEcho": None, "iTotalDisplayRecords": 0})


#class TestRestGameCrud(unittest.TestCase):
#    def __init__(self, *args, **kwargs):
#        unittest.TestCase.__init__(self, *args, **kwargs)
#        self.app = webtest()
#
#    def setUp(self):
#        self.app.post('/torpedo/rest/resetdb')
#        # WHEN user logs in 
#        ret = self.app.post('/torpedo/default/user/login',
#                      {'username': 'admin',
#                       'password': 'minda'})
#        self.assertEquals(ret.status, '200 OK')
#
#    def test_game_create(self):
#        res = self.app.post('/torpedo/rest/game/create',
#            {
#             'fields' : 'home_id,location,date,guest_id',
#             'values' : '1,Location test,2012-10-10 11:00:00,2'
#            })
#        self.assertEquals(res.status, '200 OK')
#        res = self.app.get('/torpedo/rest/game/list')
#        self.assertEquals(json.loads(res.body),
#                          [{'id': 1, 'home_id': 1, 'guest_id': 2,
#                           'date': '2012-10-10 11:00:00',
#                           'location': 'Location test'}])
#        res = self.app.get('/torpedo/rest/game/dlist')
#        self.assertEquals(json.loads(res.body), {'iTotalRecords': 1,
#                                     'aaData': [[1, 1, 2,
#                                                 '2012-10-10T11:00:00',
#                                                 'Location test']],
#                                     'sEcho': None,
#                                     'iTotalDisplayRecords': 1})
#
#    def test_game_delete(self):
#        # GIVEN empty db with admin user
#        # AND user creates a game
#        res = self.app.post('/torpedo/rest/game/create',
#            {
#             'fields' : 'home_id,location,date,guest_id',
#             'values' : '1,Location test,2012-10-10 11:00:00,2'
#            })
#        self.assertEquals(res.status, '200 OK')
#        # THEN game is created 
#        res = self.app.get('/torpedo/rest/game/list')
#        self.assertEquals(json.loads(res.body),
#                          [{'id': 1, 'home_id': 1, 'guest_id': 2,
#                            'date': '2012-10-10 11:00:00',
#                            'location': 'Location test'}])
#        # AND WHEn game is deleted  
#        res = self.app.post('/torpedo/rest/game/delete/1/')
#        # THEN it is no longer found
#        res = self.app.get('/torpedo/rest/game/list')
#        self.assertEquals(json.loads(res.body), [])
#
#    def test_game_view(self):
#        # GIVEN empty db with admin user
#        # AND user creates a team
#        res = self.app.post('/torpedo/rest/team/create',
#            {
#             'fields' : 'name',
#             'values' : 'test team'
#            })
#        # AND user creates a game
#        res = self.app.post('/torpedo/rest/game/create',
#            {
#             'fields' : 'home_id,location,date',
#             'values' : '1,Location test,2012-10-10 11:00:00'
#            })
#        self.assertEquals(res.status, '200 OK')
#        # THEN game is created 
#        res = self.app.get('/torpedo/rest/gameview/dlist?sQuery=id==1')
#        self.assertEquals(json.loads(res.body), {'iTotalRecords': 1,
#                                     'aaData': [[1, u'2012-10-10T11:00:00', u'Location test', u'test team', 1, u'-', u'-', 0, 0]],
#                                     'sEcho': None, 'iTotalDisplayRecords': 1})
#
#    def test_team_view(self):
#        # GIVEN empty db with admin user
#        # AND user creates a teams
#        self.app.post('/torpedo/rest/team/create',
#            {
#             'fields' : 'name',
#             'values' : 'test team1'
#            })
#        self.app.post('/torpedo/rest/team/create',
#            {
#             'fields' : 'name',
#             'values' : 'test team2'
#            })
#        # THEN team list
#        res = self.app.get('/torpedo/rest/team/dict?fields=name')
#        self.assertEquals(json.loads(res.body), {'1': 'test team1', '2': 'test team2'})
#class TestRestGoalCrud(unittest.TestCase):
#    def __init__(self, *args, **kwargs):
#        unittest.TestCase.__init__(self, *args, **kwargs)
#        self.app = webtest()
#
#    def setUp(self):
#        self.app.post('/torpedo/rest/resetdb')
#        # WHEN user logs in 
#        ret = self.app.post('/torpedo/default/user/login',
#                      {'username': 'admin',
#                       'password': 'minda'})
#        self.assertEquals(ret.status, '200 OK')
#
#    def test_goal_create(self):
#        # GIVEN existing team and game 
#        res = self.app.post('/torpedo/rest/team/create',
#            {
#             'fields' : 'name',
#             'values' : 'test team1'
#            })
#        self.assertEquals(res.status, '200 OK')
#        res = self.app.post('/torpedo/rest/game/create',
#            {
#             'fields' : 'home_id,location,date',
#             'values' : '1,Location test,2012-10-10 11:00:00'
#            })
#        self.assertEquals(res.status, '200 OK')
#        # WHEN creating a two goals
#        res = self.app.post('/torpedo/rest/goal/create',
#            {
#             'fields' : 'team_id,game_id,time',
#             'values' : '1,1,00:00:00'
#            })
#        res = self.app.post('/torpedo/rest/goal/create',
#            {
#             'fields' : 'team_id,game_id,time',
#             'values' : '1,1,00:10:11'
#            })
#        self.assertEquals(res.status, '200 OK')
#        res = self.app.get('/torpedo/rest/goal/dlist?iSortingCols=1&iSortCol_0=1&sSortDir_0=asc')
#        self.assertEquals(json.loads(res.body),
#                          {'iTotalRecords': 2,
#                            'aaData': [[1, '00:00:00', 1, 1, '-', '-', '-'],
#                                       [2, '00:10:11', 1, 1, '-', '-', '-'],
#                                       ],
#                            'sEcho': None,
#                            'iTotalDisplayRecords': 2})
#        res = self.app.get('/torpedo/rest/goalview/dlist?iSortingCols=1&iSortCol_0=1&sSortDir_0=asc')
#        self.assertEquals(json.loads(res.body),
#                          {'iTotalRecords': 2,
#                            'aaData': [[1, '00:00:00', '-', u'test team1', [u'Location test', u'2012-10-10T11:00:00'], '-', '-'],
#                                       [2, '00:10:11', '-', u'test team1', [u'Location test', u'2012-10-10T11:00:00'], '-', '-'],
#                                       ],
#                            'sEcho': None,
#                            'iTotalDisplayRecords': 2})
#
#    def test_goal_view_query(self):
#        # GIVEN existing team and two games 
#        res = self.app.post('/torpedo/rest/team/create',
#            {
#             'fields' : 'name',
#             'values' : 'test team1'
#            })
#        self.assertEquals(res.status, '200 OK')
#        res = self.app.post('/torpedo/rest/game/create',
#            {
#             'fields' : 'home_id,location,date',
#             'values' : '1,Location test,2012-10-10 11:00:00'
#            })
#        res = self.app.post('/torpedo/rest/game/create',
#            {
#             'fields' : 'home_id,location,date',
#             'values' : '1,Location test,2012-10-10 13:00:00'
#            })
#        self.assertEquals(res.status, '200 OK')
#        # WHEN creating a two goals to separate games
#        res = self.app.post('/torpedo/rest/goal/create',
#            {
#             'fields' : 'team_id,game_id,time',
#             'values' : '1,1,00:00:00'
#            })
#        res = self.app.post('/torpedo/rest/goal/create',
#            {
#             'fields' : 'team_id,game_id,time',
#             'values' : '1,2,00:10:11'
#            })
#        self.assertEquals(res.status, '200 OK')
#        # WHEN requesting goals from first game
#        res = self.app.get('/torpedo/rest/goal/dlist?sQuery=game_id==1 and team_id==1')
#        self.assertEquals(json.loads(res.body),
#                          {'iTotalRecords': 1,
#                            'aaData': [[1, '00:00:00', 1, 1, '-', '-', '-'],
#                                       ],
#                            'sEcho': None,
#                            'iTotalDisplayRecords': 1})
#
#
#class TestRestPlayerCrud(unittest.TestCase):
#    def __init__(self, *args, **kwargs):
#        unittest.TestCase.__init__(self, *args, **kwargs)
#        self.app = webtest()
#
#    def setUp(self):
#        self.app.post('/torpedo/rest/resetdb')
#        # WHEN user logs in 
#        ret = self.app.post('/torpedo/default/user/login',
#                      {'username': 'admin',
#                       'password': 'minda'})
#        self.assertEquals(ret.status, '200 OK')
#
#    def test_player_create(self):
#        # GIVEN empty db
#        # WHEN creating a player 
#        res = self.app.post('/torpedo/rest/player/create',
#            {
#             'fields' : 'name,number',
#             'values' : 'teppo t,12'
#            })
#        self.assertEquals(res.status, '200 OK')
#        # THEN the player list returns the newly created player
#        res = self.app.get('/torpedo/rest/player/list')
#        self.assertEquals(res.status, '200 OK')
#        self.assertEquals(json.loads(res.body),
#                          [{u'number': 12, 'team_id': None,
#                            'role': None, 'id': 1, 'name': 'teppo t'}])
#
#    def test_playerview(self):
#        # GIVEN empty db
#        # WHEN creating a player 
#        res = self.app.post('/torpedo/rest/player/create',
#            {
#             'fields' : 'name,number',
#             'values' : 'teppo t,12'
#            })
#        self.assertEquals(res.status, '200 OK')
#        # THEN the playerview list returns the newly created player
#        res = self.app.get('/torpedo/rest/playerview/list')
#        self.assertEquals(res.status, '200 OK')
#        self.assertEquals(json.loads(res.body),
#                          [{'name': 'teppo t',
#                            'penalties': '00:00:00',
#                            'number': 12,
#                            'assists': 0,
#                            'role': '-',
#                            'goals': 0,
#                            'team': '-',
#                            'id': 1,
#                            'points': 0}])
#        res = self.app.get('/torpedo/rest/playerview/dlist')
#        self.assertEquals(res.status, '200 OK')
#        self.assertEquals(json.loads(res.body),
#                          {'iTotalRecords': 1,
#                           'aaData': [[1, 12, 'teppo t', '-', '-',
#                                       0, 0, 0, '00:00:00']],
#                           'sEcho': None, 'iTotalDisplayRecords': 1})
#
#    def test_playerview_with_game_data(self):
#        # GIVEN empty db
#        # WHEN creating a player 
#        res = self.app.post('/torpedo/rest/player/create',
#            {
#             'fields' : 'name,number',
#             'values' : 'teppo t,12'
#            })
#        self.assertEquals(res.status, '200 OK')
#        # AND a game with goal for the player
#        res = self.app.post('/torpedo/rest/game/create',
#            {
#             'fields' : 'home_id,location,date,guest_id',
#             'values' : '1,Location test,2012-10-10 11:00:00,2'
#            })
#        self.assertEquals(res.status, '200 OK')
#        # WHEN creating a two goals
#        res = self.app.post('/torpedo/rest/goal/create',
#            {
#             'fields' : 'team_id,game_id,time,player_id',
#             'values' : '1,1,00:00:00,1'
#            })
#        res = self.app.post('/torpedo/rest/goal/create',
#            {
#             'fields' : 'team_id,game_id,time,assisting_id',
#             'values' : '1,1,00:10:11,1'
#            })
#        # AND penalties
#        res = self.app.post('/torpedo/rest/penalty/create',
#            {
#             'fields' : 'team_id,game_id,time,length,player_id',
#             'values' : '1,1,00:10:11,00:02:00,1'
#            })
#        self.assertEquals(res.status, '200 OK')
#        res = self.app.post('/torpedo/rest/penalty/create',
#            {
#             'fields' : 'team_id,game_id,time,length,player_id',
#             'values' : '1,1,00:10:11,00:10:00,1'
#            })
#        self.assertEquals(res.status, '200 OK')
#
#        # THEN the playerview list returns the newly created player with
#        # goals, points and assists
#        res = self.app.get('/torpedo/rest/playerview/list')
#        self.assertEquals(res.status, '200 OK')
#        self.assertEquals(json.loads(res.body),
#                          [{'name': 'teppo t',
#                            'penalties': '00:12:00',
#                            'number': 12,
#                            'assists': 1,
#                            'role': '-',
#                            'goals': 1,
#                            'team': '-',
#                            'id': 1,
#                            'points': 2}])
