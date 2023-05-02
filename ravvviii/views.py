from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data = {
        'title':'Home Page',
        'bdata':'welcome to b data',
        'clist':['java','c++','php'],
        'student_details':[
        {'name':'pradeep','phone_number':9865615618},
        {'name':'rohan','phone_number':9876255618}
        ]
    }
    return render(request,"index.html",data)




def aboutUs(request):
    return HttpResponse("Welcome to AboutUS page")


def course(request):
    return HttpResponse("Welcome to course page")



def courseDetail(request,courseid):
    return HttpResponse(courseid)