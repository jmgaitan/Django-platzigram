

#Django
from django.shortcuts import render

from datetime import datetime

posts= [
 {
    'title':'the best',
    'user':{
        'name':'mont Blac',
        'picture':'https://picsum.photos/id/237/200/300'
    },     
     'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
     'photo':'https://picsum.photos/800/600?image=1036',
     
 },
  {
    'title':'the b33t',
    'user':{
        'name':'datse',
        'picture':'https://picsum.photos/id/5/200/300'
    },     
     'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
     'photo':'https://picsum.photos/800/600?image=1038',
     
 }
]


def list_posts(request):
   return render(request,'feed.html', {'posts':posts})

   """el Request le da contexto al templete. luego el nombre del templates y luego en 3er lugar le podemos pasar diccionarios con datos que se accedan desde el HTML"""
    

# Create your views here.
