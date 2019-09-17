from django.shortcuts import render

posts = [
    {
        'author' : 'Lewis HM',
        'title' : 'How to be Involved',
        'content' : 'Dummy status yacho',
        'posted_on': '21 August 2019'
    },
    {
        'author': 'Hon HM',
        'title': 'How to be Independent',
        'content': 'Relation status yacho',
        'posted_on': '21 June 2015'
    },
    {
        'author': 'Leer oy ',
        'title': 'Anonymously Involved',
        'content': 'Restricted',
        'posted_on': '12 Dec 2009'
    }


]
def home(request):
    context = {
        'posts' : posts
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})