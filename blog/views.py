from django.shortcuts import render

posts = [
    {
        'author': 'TolaO',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'September 30, 2019',
    },
    {
        'author': 'DorcasO',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'September 31, 2019',
    }
]

def home(request):
    context = {
        'posts': posts
    }
    #have access to the content in the home templete
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About!'})
