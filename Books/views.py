from django.shortcuts import render,redirect
from django.views.generic import View
from Books import forms
from Books import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
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
        

class BookDetail(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        data=models.Book.objects.get(id=id)
        return render(request,"book_details.html",{"data":data})
    
class BookEdit(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("id")
        data = models.Book.objects.get(id=id)
        form = forms.BookAdd(instance=data)
        return render(request,"book_edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id = kwargs.get("id")
        data=models.Book.objects.get(id=id)
        form = forms.BookAdd(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('list')
        else:
            return render(request,"book_edit.html",{"form":form})
        

class RegistrationView(View):

    def get(self,request,*args,**kwargs):
        form = forms.RegistrationForm()
        return render(request,"registration.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect('signup')
        else:
            return render(request,"registration.html",{"form":form})
        
class SignupView(View):
    def get(self,request,*args,**kwargs):
        form = forms.SigninForm()
        return render(request,"signin.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=forms.SigninForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect('home')
        return render(request,'signin.html',{"form":form})
    
class Signout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('signin')
        
