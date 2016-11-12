from django.shortcuts import render
from markdown import markdown
from demo01.models import Post, Category
# Create your views here.


def index(request):
    print('hello')
    # for post in posts:
    #     post.body = markdown(post.body)
    dic = {
        'body': 'hello',
    }
    return render(request, 'demo01/index.html', dic)


def mark(request):
    body = Post.objects.all()[0].body
    body = markdown(body)
    print('mark', body)
    dic = {
        'body': body,
    }
    return render(request, 'demo01/mark.html', dic)
