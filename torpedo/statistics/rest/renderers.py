'''
Created on 2.7.2012

@author: teerytko
'''

from djangorestframework.renderers import BaseRenderer, get_media_type_params,\
DateTimeAwareJSONEncoder, json


class DListRenderer(BaseRenderer):
    """
    Renderer which serializes to data to data list format specific to the
    jquery Table.
    """

    media_type = 'application/dlist'
    format = 'dlist'

    def render(self, obj=None, media_type=None):
        """
        Renders *obj* into serialized JSON.
        """
        if obj is None:
            return ''

        # If the media type looks like 'application/json; indent=4', then
        # pretty print the result.
        indent = get_media_type_params(media_type).get('indent', None)
        sort_keys = False
        try:
            indent = max(min(int(indent), 8), 0)
            sort_keys = True
        except (ValueError, TypeError):
            indent = None

        return json.dumps(obj, cls=DateTimeAwareJSONEncoder, indent=indent, 
                          sort_keys=sort_keys)