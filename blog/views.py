from django.shortcuts import render

posts = [
    {
        'author': 'Rudy',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'January 4th, 2023'
    },
    {
        'author': 'Billiam',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'January 6th, 2023'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
