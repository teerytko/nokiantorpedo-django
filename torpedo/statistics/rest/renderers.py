'''
Created on 2.7.2012

@author: teerytko
'''

from djangorestframework.renderers import TemplateRenderer, JSONRenderer
from django.template import RequestContext, loader



class DListRenderer(TemplateRenderer):
    """
    Renderer which serializes to data to data list format specific to the
    jquery Table.
    """

    media_type = 'application/dlist'
    format = 'dlist'
    template = 'dlist.txt'

    def render(self, obj=None, media_type=None):
        """
        Renders *obj* using the :attr:`template` specified on the class.
        """
        if obj is None:
            return ''
        listobj = obj
        if not isinstance(listobj, list):
            listobj = [obj] 
            
        data = JSONRenderer(self.view).render(obj)

        template = loader.get_template(self.template)
        context = RequestContext(self.view.request, {
                         'request': self.view.request,  
                         'response': self.view.response,
                         'object': obj,
                         'data' : data})
        return template.render(context)
    