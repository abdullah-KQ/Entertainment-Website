from django.shortcuts import render
from .form import AddArticle

# Create your views here.
def home(request):
    
    return render(request, 'MainApp/home.html')

def article(request):
    form = AddArticle
    print(form)
    return render(request, 'MainApp/article.html',{'form':form})
