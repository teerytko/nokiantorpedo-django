
from statistics.rest.utils import get_columns
from djangorestframework.mixins import ListModelMixin, PaginatorMixin
from djangorestframework.views import InstanceModelView, ListOrCreateModelView
from djangorestframework.renderers import BaseRenderer
from statistics.rest.renderers import DListRenderer
from django.db.models.fields import TextField
from django.db.models.fields.related import ForeignKey

from django.db.models import Q


class MyInstanceModelView(InstanceModelView):
    """
    A view which extra renderers.
    """
    renderers = (list(InstanceModelView.renderers) + [DListRenderer])


class SearchModelMixin(ListModelMixin, PaginatorMixin):
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


class DataTableMixin(ListModelMixin):
    """
    List a set of `model` instances on GET requests based on
    input arguments of DataTables.
    """
    def get_ordering(self):
        return None

    def get_query(self, request, *args, **kwargs):
        """
        Create a query object for the request.

        @param sSearch: search parameter which is searched from all
        TextFields of the model.
        """
        kwargs = request.GET
        query = Q()
        sSearch = kwargs.get('sSearch')
        if sSearch is not None:
            for field in self._resource.model._meta.fields:
                if isinstance(field, TextField):
                    query |=  Q(**{'{0}__{1}'.format(field.attname, 'contains'): sSearch})
                elif isinstance(field, ForeignKey):
                    query |=  Q(**{'{0}__{1}'.format(field.name, 'name__contains'): sSearch})
        return query

    def get(self, request, *args, **kwargs):
        """
        Get the data for the request.
        """
        queryset = self.get_queryset()
        query = self.get_query(request, *args, **kwargs)
        queryset = queryset.filter(query)
        return queryset


class ListSearchModelView(DataTableMixin, ListOrCreateModelView):
    """
    A view which provides default operations for searchable list, against a 
    model in the database.
    """
    renderers = (list(InstanceModelView.renderers) + [DListRenderer])

    _suffix = 'List'

