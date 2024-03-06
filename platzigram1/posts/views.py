from django.http import HttpResponse
# Create your views here.
from datetime import datetime
import json

posts =[
    {
        'name': 'Celia Vargas',
        'user': 'cevl123',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M:%S hrs'),
        'picture': 'http://picsum.photos/200/200/?image=1036',
    },

    {
        'name': 'Lourdes López',
        'user': 'lou123',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M:%S hrs'),
        'picture': 'http://picsum.photos/200/200/?image=903',
    },
    {
        'name': 'Abigail Alvarado',
        'user': 'aby123',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M:%S hrs'),
        'picture': 'http://picsum.photos/200/200/?image=1076',
    },
]

def list_posts(request):
    """List existing posts"""
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src="{picture}"/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))
