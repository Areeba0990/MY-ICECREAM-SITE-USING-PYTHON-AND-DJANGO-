from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")

def softicecream(request):
    return render(request, 'softicecream.html')
def deal(request):
    return render(request, 'deal.html')
    # return HttpResponse("this is deal page")
def familypack(request):
    return render(request, 'familypack.html')
     #return HttpResponse("this is familypack page")
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.now())
        contact.save()

    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")
