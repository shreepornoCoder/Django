from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d = {"author":"shree", "age":35, "lst":["python","is","best"], 
        "birthday" : datetime.datetime.now(), "courses":[
        {
            "id":1,
            "name":"django",
            "fee":10000
        },
        {
            "id":2,
            "name":"python",
            "fee":5000
        },
        {
            "id":3,
            "name":"C",
            "fee":3000
        }
    ]}
    return render(request, 'first_app/home.html', context=d)