
from djangorestframework.mixins import ListModelMixin
from djangorestframework.views import ModelView, InstanceModelView, ListOrCreateModelView
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
        return request.GET.dict()


class ListSearchModelView(SearchModelMixin, ListOrCreateModelView):
    """
    A view which provides default operations for searchable list, against a 
    model in the database.
    """
    _suffix = 'List'

