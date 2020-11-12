"""Platzigram views"""

#Django
from django.http import HttpResponse
#utilities
from datetime import datetime
import json
import ast

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('oh, hi! current server time is {now}'.format(now=str(now)))

def arrayOrdenado   (request):
    #para debugear podemos utilizar pdb y accedemos a la consola y podemos ver las variables y sus propiedades
    #import pdb;pdb.set_trace()
    ############################ Hecho por mi #################################################
    ##########   numbers = request.GET['numbers']
    ##########   numbers = numbers.split(sep= ',')
    ##########   result = list(map(int, numbers))
    ##########   rresult = sorted(result)
    ##########   return HttpResponse({'rresult:number'})
    ## si quisiera que me los devuelve en modo lista return HttpResponse(str(rresult))
    ## para que sea Json debo hacer lo siguiente

    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    ##import pdb; pdb.set_trace()
    data = {
        'status':'ok',
        'numbers':sorted_ints,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(
        json.dumps(data, indent=4),
        content_type='application/json'
        )

def say_hi(request,name,age):
    if age <12: 
        message = 'I am sorry {} {}. you are not access here for age'.format(name,age)
    else:
        message = 'Hello {}, to Welcome to Platzigram'.format(name)
    return HttpResponse(message)

    

    