from django.shortcuts import render

from.models import Book

# Create your views here.


def createBook(request):
    if request.method=='POST':
     title=request.POST.get('title')
     price=request.POST.get('price')
     book=Book(title=title,price=price)

     book.save()
     return render(request,'book.html')






