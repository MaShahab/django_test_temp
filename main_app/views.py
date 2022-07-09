from django.shortcuts import render

def index(request):
    return render(request, "website/index.html")

def about(request):
    return render(request, "website/about.html")

def services(request):
    return render(request, "website/services.html")

def contact(request):
    return render(request, "website/contact.html")

def portfolio(request):
    return render(request, "website/portfolio.html")

def team(request):
    return render(request, "website/team.html")

def blog(request):
    return render(request, "website/blog.html")

