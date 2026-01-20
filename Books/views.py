from django.shortcuts import render,redirect
from django.views.generic import View
from Books import forms
from Books import models

# Create your views here.
class WelcomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'welcome.html')
    
class BookListView(View):
    def get(self,request,*args,**kwargs):
        qs=models.Book.objects.all()
        return render(request,"book.html",{"data":qs})
    
class BookAddView(View):
    def get(self,request,*args,**kwargs):
        form = forms.BookAdd()
        return render(request,"book_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form = forms.BookAdd(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
        else:
            return render(request,"book_add.html",{"form":form})
        


