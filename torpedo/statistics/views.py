from django.template import Context, loader
from django.http import HttpResponse

def players(request):
    t = loader.get_template('statistics/players.html')
    c = Context({
    })
    return HttpResponse(t.render(c))