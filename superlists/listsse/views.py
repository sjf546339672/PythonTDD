from django.http import HttpResponse
from django.shortcuts import render
from .models import StudentModel


def home_page(request):
    # return HttpResponse(b"<html><title>To-Do lists</title></html>")
    # return render(request, "home.html")

    # if request.method == 'POST':
    #     return HttpResponse(request.POST['item_text'])
    # return render(request, 'home.html')
    return render(request, 'home.html',
                  {'new_item_text': request.POST.get('item_text', ''), })


def index(request):
    student = StudentModel.objects.all()
    print("==========={}".format(student))
    return HttpResponse("aaaa: {}".format(student))




