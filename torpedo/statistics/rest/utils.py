'''
Created on 11.8.2012

@author: teerytko
'''


def to_dlist(list_of_dicts, columns=None):
    """
    Convert a list of dictionaries to a list of lists
    with the values of the dictionaries.
    Expects that each dictionary in the list has same keys.
    @param list_of_dicts: the list of dictionaries
    @param columns: given columns order
    """
    data = []
    if columns is None and len(list_of_dicts) > 0:
        columns = list_of_dicts[0].keys()
    for obj in list_of_dicts:
        row = []
        for col in columns:
            row.append(obj.get(col))
        data.append(row)
    return data

def get_columns(request):
    try:
        cols = request.GET['sColumns']
        columns = [col for col in cols.split(',') if len(col) > 0]
        return columns
    except KeyError:
        # no columns given 
        return None

def get_sorting(request):
    sorting = []
    for i in range(10):
        if 'iSortCol_%d' % i in request.GET:
            sorting.append((int(request.GET['iSortCol_%d' % i]),
                            request.GET['sSortDir_%d' % i] == 'desc'))
        else:
            break;
    return sorting

