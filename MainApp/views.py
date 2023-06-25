from django.shortcuts import render

# Create your views here.
def home(request):
    
    return render(request, 'MainApp/home.html')

def article(request):
    return render(request, 'MainApp/article.html')
