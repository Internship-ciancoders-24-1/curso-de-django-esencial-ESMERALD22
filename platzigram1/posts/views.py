from django.http import HttpResponse
# Create your views here.
from datetime import datetime
import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

posts =[
    {
        'title': 'Mont Blanc',
        'user':{
            'name': 'Celia Vargas',
            'picture': 'http://picsum.photos/60/60/?image=1027',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M:%S hrs'),
        'photo': 'http://picsum.photos/200/200/?image=1036',
    },

    {
        'title': 'Vía Láctea',
        'user':{
            'name': 'Lourdes López',
            'picture': 'http://picsum.photos/60/60/?image=1005',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M:%S hrs'),
        'photo': 'http://picsum.photos/200/200/?image=903',
    },

    {
        'title': 'Nuevo auditorio',
        'user':{
            'name': 'Samuel López',
            'picture': 'http://picsum.photos/60/60/?image=883',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M:%S hrs'),
        'photo': 'http://picsum.photos/200/200/?image=1076',
    },

]

@login_required
def list_posts(request):
    """List existing posts"""
    #content = []
    #for post in posts:
    #   content.append("""
    #        <p><strong>{name}</strong></p>
    #        <p><small>{user} - <i>{timestamp}</i></small></p>
    #        <figure><img src="{picture}"/></figure>
    #   """.format(**post))
    #return HttpResponse('<br>'.join(content))

    return render(request, 'posts/feed.html',{'posts':posts})
