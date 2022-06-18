from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .form import ArticleForm
from .models import Article

# Create your views here.
def article_search_view(request):
    # print(dir(request))
    # print(request.GET)

    query_dict = request.GET #THIS IS A DICTIONARY
    # query = query_dict.get("q") #<input type="text" name="q"/
    try:
         query = int(query_dict.get("q"))
    except:
        query = None
    article_obj = None
    if(query is not None):
        article_obj = Article.objects.get(id=query)

    context = {
        "object": article_obj,
    }
    return render(request, "articles/search.html", context=context)

@login_required
def article_create_view(request.Post or None):
    # print(request.POST)
    form = ArticleForm
    # print(dir(form))
    context = {
        "form": form
    }
    if form.is_valid():
        title = form.cleaned_data.get('title')
        content = form.cleaned_data.get('content')
        article_object = Article.objects.create(title=title, content=content)
        print(title, content)
        context['object'] = article_object
        context['created'] = True
    return render(request, "articles/create.html", context=context)

##VERSION 2
# def article_create_view(request):
#     # print(request.POST)
#     form = ArticleForm
#     # print(dir(form))
#     context = {
#         "form": form
#     }
#     if request.method == "POST":
#         form = ArticleForm(request.POST)
#         context['form'] = form
#         if form.is_valid():
#             title = form.cleaned_data.get('title')
#             content = form.cleaned_data.get('content')
#             article_object = Article.objects.create(title=title, content=content)
#             print(title, content)
#             context['object'] = article_object
#             context['created'] = True
#     return render(request, "articles/create.html", context=context)

##VERSION 1
# def article_create_view(request):
#     # print(request.POST)
#     context = {}
#     if request.method == "POST":
#         title = request.POST.get('title')
#         content = request.POST.get('content')
#         article_object = Article.objects.create(title=title, content=content)
#         # print(title, content)
#         context['object'] = article_object
#         context['created'] = True
#     return render(request, "articles/create.html", context=context)

def article_detail_view(request, id=None):
    article_obj = None

    if id is not None:
        article_obj = Article.objects.get(id=id)

    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context)
