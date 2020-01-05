from django.shortcuts import render
from .models import Book
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import CreateView
from . forms import BookForm

# Create your views here.

def home(request):
	return render(request, 'home.html', {})

def save_book(request):
	if request.method == 'POST':
		book = Book.objects.get_or_create(
			name=request.POST.get('name'),price=request.POST.get('price'),pages=request.POST.get('pages')
			)

		data={
			'book':book
		}
		return JsonResponse(data)
		# #try:
		# 	#book.save()
		# 	#return HttpResponse('Book Saved')
		# #xcept:
		# 	#return HttpResponse('Sorry some error occured') open console wait 
		
		# return HttpResponse('Book Save Successfully')

		

