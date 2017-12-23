"""
Definition of views.
"""

from django.shortcuts import render, render_to_response, redirect, HttpResponseRedirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime, time
from app.models import article, Nuser
from django.template.context_processors import csrf
import time
from django.core.paginator import Paginator
from django.contrib import auth
def registration(request):
    return render_to_response('app/registration.html')
def cop(request):
    return render_to_response('app/copyrighting.html')
def exit(request):
  if request.user.is_authenticated():
    auth.logout(request)
    return redirect('/login')
  else:
    return redirect('/login')
def login(request):
    args={}
    args.update(csrf(request))
    if request.user.is_authenticated():
     return redirect('/adminpanel')
    else:
     if request.POST:
        login=request.POST.get('login','')
        password=request.POST.get('password','')
        user=auth.authenticate(username=login,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/adminpanel')
        else:
            args['login_error']='Неверный логин или пароль'
            return render_to_response('app/authorization.html',args)
     else:
        return render_to_response('app/authorization.html',args)
def skyway(request):
    return render_to_response('app/skyway.html')
def articles(request,number):
    art=article.objects.get(id=number)
    return render_to_response('app/post.html',{'art':art})
def main(request,page_number=1):
    allarticles=article.objects.all().order_by('-id')
    k=article
    for k in allarticles:
        if len(k.text)<=1000:
            k.poster=k.text
        else:
            l=k.text
            for i in range(999, len(l)):
                if l[i]==' ':
                    k.poster=l[:i+1]+'...'
                    break
    current_page=Paginator(allarticles,5)
    return render_to_response('app/main.html',{'articles':current_page.page(page_number)})
def delete(request):
  if request.user.is_authenticated():
    i=request.GET.get('id')
    art=article.objects.get(id=i)
    art.delete()
    return redirect('/adminpanel')
  else:
      return redirect('/login')
def adminpanel(request):
  if request.user.is_authenticated():
    articles=article.objects.all().order_by('-id')
    if request.POST:
        article(subject=request.POST.get('title'),preview=request.POST.get('image'),text=request.POST.get('TextArea1'),date=str(time.strftime("%d-%m-%Y", time.localtime()))).save()
        return redirect('/adminpanel')
    else:
        return render(request,'app/posting.html',{'articles':articles})
  else:
      return redirect('/login')
def about(request):
    return render_to_response('app/about.html')
