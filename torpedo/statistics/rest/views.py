
from djangorestframework.mixins import ListModelMixin
from djangorestframework.views import InstanceModelView, ListOrCreateModelView
from djangorestframework.renderers import BaseRenderer
from statistics.rest.renderers import DListRenderer

class MyInstanceModelView(InstanceModelView):
    """
    A view which extra renderers.
    """
    renderers = (list(InstanceModelView.renderers) + [DListRenderer])


class SearchModelMixin(ListModelMixin):
    """
    Behavior to list a set of `model` instances on GET requests
    """
    def get_query_kwargs(self, request, *args, **kwargs):
        """
        """
        kwargs = request.GET.dict()
        # pop possible echo parameter
        kwargs.pop('sEcho', None)
        # If the URLconf includes a .(?P<format>\w+) pattern to match against
        # a .json, .xml suffix, then drop the 'format' kwarg before
        # constructing the query.
        if BaseRenderer._FORMAT_QUERY_PARAM in kwargs:
            del kwargs[BaseRenderer._FORMAT_QUERY_PARAM]

        return kwargs


class ListSearchModelView(SearchModelMixin, ListOrCreateModelView):
    """
    A view which provides default operations for searchable list, against a 
    model in the database.
    """
    renderers = (list(InstanceModelView.renderers) + [DListRenderer])

    _suffix = 'List'

