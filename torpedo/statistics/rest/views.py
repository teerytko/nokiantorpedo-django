
from djangorestframework.mixins import ListModelMixin, PaginatorMixin, ModelMixin,InstanceMixin, ReadModelMixin, DeleteModelMixin
from djangorestframework.views import InstanceModelView, ListOrCreateModelView, ModelView
from djangorestframework.renderers import BaseRenderer
from statistics.rest.renderers import DListRenderer, DictRenderer
from django.db.models.fields import TextField
from django.db.models.fields.related import ForeignKey

from django.db.models import Q

class MyUpdateModelMixin(ModelMixin):
    """
    Behavior to update a `model` instance on PUT requests that accepts
    individual field updates
    """
    def put(self, request, *args, **kwargs):
        model = self.resource.model
        query_kwargs = self.get_query_kwargs(request, *args, **kwargs)

        # TODO: update on the url of a non-existing resource url doesn't work
        # correctly at the moment - will end up with a new url
        try:
            self.model_instance = self.get_instance(**query_kwargs)
            self.update = self.DATA.dict()
            self.basedata = self.DATA.dict()
            for field in self.model_instance._meta.fields:
                self.basedata.setdefault(field.attname, getattr(self.model_instance, field.attname))
            self._content = self.validate_request(self.basedata, self.FILES)
            self.model_instance = self.get_instance(**query_kwargs)
            for (key, val) in self.update.items():
                if key:
                    setattr(self.model_instance, key, val)
        except model.DoesNotExist:
            self.model_instance = model(**self.get_instance_data(model, self.CONTENT, *args, **kwargs))
        self.model_instance.save()
        return self.model_instance

    @property
    def CONTENT(self):
        """
        Returns the cleaned, validated request content.

        May raise an :class:`response.ErrorResponse` with status code 400 (Bad Request).
        """
        if not hasattr(self, '_content'):
            self._content = self.validate_request(self.basedata, self.FILES)
        return self._content

class MyInstanceModelView(InstanceMixin, ReadModelMixin, MyUpdateModelMixin, DeleteModelMixin, ModelView):
    """
    A view which provides default operations for read/update/delete against a model instance.
    """
    renderers = (list(InstanceModelView.renderers) + [DListRenderer])
    _suffix = 'Instance'


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
        sQuery = kwargs.get('sQuery')
        if sQuery is not None:
            queryparams = {}
            for queryitem in sQuery.split(' and '):
                key, value = queryitem.split('==')
                queryparams[key] = value
            query |= Q(**queryparams)
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
    renderers = (list(InstanceModelView.renderers) + [DListRenderer, DictRenderer])

    _suffix = 'List'

