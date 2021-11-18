from django.shortcuts import render
from .models import Post

def home_view(request):
    context = {}

    post = Post.objects.all()
    context["posts"] = post
    
    return render(request, "home.html", context)

def about_view(request):
    context = {}
    context["Nama"] = "Ofi"
    context["Asal"] = "Padang"
    context["Tinggi"] = "158"
    context["BB"] = "57"

    return render(request, "about.html", context)
