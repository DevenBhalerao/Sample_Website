from django.shortcuts import render

# Create your views here.
def index(request):

	context = {

	}
	render(request, 'templates/index.html', context)