'''
Created on 2.7.2012

@author: teerytko
'''


from operator import itemgetter
from statistics.rest.utils import to_dlist, get_columns, get_sorting
from djangorestframework.renderers import TemplateRenderer, JSONRenderer
from django.template import RequestContext, loader

class DListRenderer(TemplateRenderer):
    """
    Renderer which serializes to data to data list format specific to the
    jquery Table.
    """

    media_type = 'text/plain'
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
        
        columns = get_columns(self.view.request)
        sorting = get_sorting(self.view.request)
        dl = to_dlist(obj, columns)
        for order in sorting:
            dl.sort(key=itemgetter(order[0]), reverse=order[1])
        data = JSONRenderer(self.view).render(dl)
        template = loader.get_template(self.template)
        context = RequestContext(self.view.request, {
                         'echo': self.view.request.GET.get('sEcho'),  
                         'request': self.view.request,  
                         'response': self.view.response,
                         'object': listobj,
                         'data' : data})
        return template.render(context)
    
