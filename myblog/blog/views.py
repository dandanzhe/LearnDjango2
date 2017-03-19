from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from blog.models import Article
# Create your views here.


def index(request):
    return render(request, 'blog/index.html', {'article': Article.objects.all()})


def article_getpage(request, article_id):
    return render(request, 'blog/page.html',{'article': Article.objects.get(id=article_id)})


def edit_page(request,article_id):
    if str(article_id)=='0':
        return render(request, 'blog/edit_page.html')
    return render(request, 'blog/edit_page.html',{'article': Article.objects.get(id=article_id)})


def edit_page_action(request):
    title = request.POST.get('title', 'TITLE')
    if title == "":
        title = 'TITLE'
    content = request.POST.get('content', 'CONTENT')
    if content == "":
        content = 'content'
    article_id = request.POST.get('article_id','0')
    if str(article_id) == '0':
        Article.objects.create(title=title, content=content)
        return HttpResponseRedirect('/index/index')
    article = Article.objects.get(id=article_id)
    article.title = title
    article.content = content
    article.save()
    return HttpResponseRedirect('/index/pages/%d'%article.id)

def page_delete(request,article_id):
    Article.objects.get(id=article_id).delete()
    return HttpResponseRedirect('/index/index')
