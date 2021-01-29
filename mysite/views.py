from django.views.generic import TemplateView, FormView
from mysite.forms import PostSearchForm
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import os

from stock.models import Post


class HomeView(TemplateView):
    template_name = 'home.html'


def stock_db(request):
    stock = Post.objects.all().order_by('-id')[0]
    context = {'stocks': stock}

    return render(request, 'home.html', context)


@method_decorator(csrf_exempt)
def form_valid(request):
    print(request)
    os.chdir('C:/Users/User/Desktop/DataStudy/Project/django_stock_web/yahoo_stock')
    os.system("scrapy crawl stock")

    return render(request, 'search.html')

# class SearchLV(FormView):
#     form_class = PostSearchForm
#     template_name = "search.html"