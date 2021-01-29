from django.views.generic import TemplateView, FormView
from mysite.forms import PostSearchForm
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import os

from stock.models import Post


class HomeView(TemplateView):
    template_name = 'home.html'


@method_decorator(csrf_exempt)
def form_valid(request):
    symbol = request.POST.get('symbol')
    print(symbol)

    # os.chdir('C:/Users/User/Desktop/DataStudy/Project/django_stock_web/yahoo_stock/spiders/stock.py')
    # os.system("symbol_name = %s" % symbol)

    os.chdir('C:/Users/User/Desktop/DataStudy/Project/django_stock_web/yahoo_stock')
    os.system("scrapy crawl stock")

    stock = Post.objects.all().order_by('-id')[0]
    context = {'stocks': stock}

    return render(request, 'search.html', context)
