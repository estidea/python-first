from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'title': "Home"
	}
	return render(request, 'mainApp/homePage.html', context)


def contact(request):
	context = {
		'values': ['Nick','+312234555'],
		'title': "Contact me"
	}
	return render(request, 'mainApp/contact.html',context)

def about(request):
	return render(request, 'mainApp/about.html')