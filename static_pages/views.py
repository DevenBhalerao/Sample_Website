from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, "index.html", {})

def about(request):
	return render(request, "about.html", {})

def sidebar_left(request):
	return render(request, "sidebar-left.html", {})

def sidebar_right(request):
	return render(request, "sidebar-right.html", {})