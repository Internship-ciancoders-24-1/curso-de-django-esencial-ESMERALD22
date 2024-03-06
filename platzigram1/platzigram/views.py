

from django.http import HttpResponse
#utilites
from datetime import datetime
import json
def hello_world(request):
    """Esta funcion devuelve un saludo"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M:%S hrs')
    return HttpResponse("Hi! Current server time is {now}".format(now=now)) 

def hi(request):
    numbers_str = request.GET.get('numbers', '')  
    numbers_list = [int(num) for num in numbers_str.split(',')]  
    sorted_numbers = sorted(numbers_list)  
    return HttpResponse(json.dumps(sorted_numbers), content_type='application/json') 

def solucion(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_numbers = sorted(numbers)
    data ={
        'status': 'success',
        'numbers': sorted_numbers,
        'mesagger': 'Intgers sorted successfully',
    }
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type = 'application/json'
    )


def say_hi(request, name, age):
    if age < 12:
        message ="Sorry {}, you are not allow here".format(name)
    else:
        message ="Hi {}, Welcom to Platzigram".format(name)

    return HttpResponse(
        message,
    )