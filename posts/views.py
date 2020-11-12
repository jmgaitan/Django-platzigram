

#Django
from django.http import HttpResponse
from datetime import datetime

posts= [
 {
     'name':'mont Blac',
     'user':'Yesica Cortes',
     'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
     'picture':'https://picsum.photos/id/2/400/600'
 }
]


def list_posts(request):
    """List existing posts."""
    content =[]
    for post in posts:
        content.append("""
        <p><strong>{name}</strong></p>
        <p><small>{user}-<i>{timestamp}</i></small></p>
        <figure><img src="{picture}"/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))

# Create your views here.
