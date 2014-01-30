'''
Created on 2.7.2012

@author: teerytko
'''


from operator import itemgetter
from statistics.rest.utils import to_dlist, get_columns, get_sorting, to_dict
from djangorestframework.renderers import TemplateRenderer, JSONRenderer
from django.template import RequestContext, loader

def multikeysort(items, columns):
    from operator import itemgetter
    comparers = [ ((itemgetter(col[1:].strip()), -1) if col.startswith('-') else (itemgetter(col.strip()), 1)) for col in columns]  
    def comparer(left, right):
        for fn, mult in comparers:
            result = cmp(fn(left), fn(right))
            if result:
                return mult * result
        else:
            return 0
    return sorted(items, cmp=comparer)

def multilistsort(items, columns):
    from operator import itemgetter
    comparers = [ ((itemgetter(col[0]), -1) if col[1]
                   else (itemgetter(col[0]), 1)) for col in columns]
    def comparer(left, right):
        for fn, mult in comparers:
            result = cmp(fn(left), fn(right))
            if result:
                return mult * result
        else:
            return 0
    return sorted(items, cmp=comparer)

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
        
        # create the dlist format with the columns in
        # given format
        columns = get_columns(self.view.request)
        dl = to_dlist(obj, columns)
        # order the elements with with request tuples
        # (orderIndex, reverse)
        sorting = get_sorting(self.view.request)
        sorteddl = multilistsort(dl, sorting)
#         
#         for order in sorting:
#             dl.sort(key=itemgetter(order[0]), reverse=order[1])
        data = JSONRenderer(self.view).render(sorteddl)
        template = loader.get_template(self.template)
        context = RequestContext(self.view.request, {
                         'echo': self.view.request.GET.get('sEcho') or 0,  
                         'request': self.view.request,  
                         'response': self.view.response,
                         'totalcount': self.view.totalcount,
                         'maxcount': self.view.maxcount,
                         'object': listobj,
                         'data' : data})
        return template.render(context)

    
class DictRenderer(TemplateRenderer):
    """
    Renderer which serializes to data to dict format
    """

    media_type = 'text/plain'
    format = 'dict'

    def render(self, obj=None, media_type=None):
        """
        Renders *obj* using the :attr:`template` specified on the class.
        """
        if obj is None:
            return ''
        listobj = obj
        if not isinstance(listobj, list):
            listobj = [obj]
        # create the dict format with the key and value
        key = self.view.request.GET.get('key')
        value = self.view.request.GET.get('value')
        dl = to_dict(obj, key, value)
        data = JSONRenderer(self.view).render(dl)
        return data

