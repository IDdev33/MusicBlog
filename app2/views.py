from django.shortcuts import render, redirect
from .models import Subscriber, Article
from django.contrib import messages


# Create your views here.

# Home
def index(request):
     Articles = Article.objects.all()
     context ={
          'Articles': Articles,
     }

     if request.method == 'POST':
      name = request.POST['name']
      email = request.POST['email']
      if Subscriber.objects.filter(Email=email).exists():
                messages.info(request, 'Email is already subscribed!')
                return render(request, 'index.html')
                
      else:
           subscriber = Subscriber.objects.create(Name=name, Email=email)
           subscriber.save();
           return redirect('News')
     else:
        return render(request, 'index.html', context)

# News
def News(request):
     return render(request, 'News.html')

# Alienware View
def DocA(request):
     article = Article.objects.filter(Name='Alienware Documentation').first()
     context ={
          'article': article
     }
     return render(request, 'DocA.html', context)

# Blog Doc View
def DocB(request):
     article = Article.objects.filter(Name='Blog Documentation').first()
     context ={
          'article': article
     }
     return render(request, 'DocB.html', context)

# Journey Doc
def JourneyDoc(request):
     article = Article.objects.filter(Name='My Web Development Journey').first()
     context ={
          'article':article
     }
     return render(request, 'JourneyDoc.html', context)


# Ai Doc
def AiDoc(request):
     article = Article.objects.filter(Name='Thoughts on A.I').first()
     context ={
          'article':article
     }
     return render(request, 'AiDoc.html', context)
