from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponse
# Create your views here.
def welcome(Request):
#     return HttpResponse("<h1 style = 'background:pink'> hello! this is my first django app </h1>")
      my_dict = {'insert_me': "i am coming from subfolder app1_homw/reg.html"}
      return render(Request, 'app1_home/reg.html', context=my_dict)
