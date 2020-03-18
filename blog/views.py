from django.shortcuts import render
from django.http import HttpResponse


posts = [
			{
				'author'     : 'Somesh Khandelia',
				'title' 	 : 'Blog Post 1',
				'content'    : 'This is the first post content.',
				'date_posted': 'March 15, 2020'
			},
			{
				'author'     : 'Yukty Khandelia',
				'title' 	 : 'Blog Post 2',
				'content'    : 'This is the second post content.',
				'date_posted': 'March 16, 2020'
			}
		]


def home(request):
	context = {
				'posts': posts,
				'title': 'Home'
			  }
	# The templates folder is automatically detected by django 
	return render(request, 'blog/home.html', context)


def about(request):
	context = {
				'title': 'About'
			  }
	return render(request, 'blog/about.html', context)
