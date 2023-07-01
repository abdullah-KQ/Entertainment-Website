from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import AddArticle
from .models import Article
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    
    return render(request, 'MainApp/home.html')

def article(request):
    Add_Article = Article.objects.all()

    if request.method == "POST":
        Add_Article.create(
            title = request.POST.get("title"),
            article_type = request.POST.get("article_type"),
            author = User.objects.get(id=request.user.id),
            body = request.POST.get("body"),
            )
        return HttpResponseRedirect("/")

    else:
        form = AddArticle()
        
    return render(request, 'MainApp/article.html',{'form':form})
