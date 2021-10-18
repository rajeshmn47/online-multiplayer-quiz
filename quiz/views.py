from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.core.paginator import Page, Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def home(request):
    q=questions.objects.all().order_by('question_text')
    paginator=Paginator(q,20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    scored=0  
    wrong=0
    correct=0
    i=score.objects.all().order_by('-scores')
    if request.method=='POST':
        print(request.POST)
        for a in q:
            if request.POST.get(a.question_text)==a.answer:
               print(a.answer)
               correct+=1
               scored+=10
            else:
                wrong+=1

        score.objects.create(scores=scored,user=request.user)
        return render(request,'results.html',{'q':scored,'c':correct,'w':wrong})
    else:
     q=questions.objects.all() 
     return render(request,'home.html',{'w':page_obj,'l':i})

def register(request):
    form=createuserform()
    if request.method=="POST":
       a=createuserform(request.POST)
       if a.is_valid():
            a.save()
       return redirect('/login')
    return render(request,'register.html',{'w':form})

def loginform(request):
    form=AuthenticationForm()
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
    return render(request,'login.html',{'w':form})

def addquestion(request):
    if request.user.username=="azib":
     form=addQuestionform()
     if request.method=="POST":
       a=addQuestionform(request.POST)
       if a.is_valid():
            a.save()
       return render(request,'addq.html',{'w':form})
     return render(request,'addq.html',{'w':form})
    else:
        return HttpResponse('u cant add question')
  
def logoutin(request):
    logout(request)
    return redirect('/login')