from django.shortcuts import render

# Create your views here.
def hellostudent(request):
    return render(request, "helloworld/mainpage.html")
