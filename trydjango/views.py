"""
To render html web pages
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article

def home_view(request, *args, **kwargs):
    """
    Take in a request(Django sends request) 
    Return HTML as a response(We pick to return the response)
    """ 
    print(id)
    name = "Chibueze" #hand coded
    random_id = random.randint(1, 2) #psueedo random

    #from the database
    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()
    # my_list = [120, 30, 50, 400]
    # article_title = article_obj.title
    # article_content = article_obj.content

    context = {
        "object_list": article_queryset,
        "title": article_obj.title,
        "content": article_obj.content,
        "id": article_obj.id,
    }
    # GET TEMPLATE
    
    HTML_STRING = render_to_string("home-view.html", context=context)

    # HTML_STRING = """
    #     <h1>{title} (id:{id})</h1>
    #     <p>{content}</p>
    # """.format(**context)
    return HttpResponse(HTML_STRING)