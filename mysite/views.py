from django.views.generic import TemplateView, FormView
from mysite.forms import PostSearchForm
from django.shortcuts import render
import os

from stock.models import Post


class HomeView(TemplateView):
    template_name = 'home.html'


class SearchLV(FormView):
    form_class = PostSearchForm
    template_name = "home.html"

    def form_valid(self, form):
        os.chdir("C:/Users/User/Desktop/DataStudy/Project/django_crawling_rest_api/yahoo_stock/yahoo_stock")
        os.system("scrapy crawl stock")

        return super().form_valid(form)

    def stock_db(self, request):
        stock = Post.objects.all().order_by('-id')[0]
        return render(self.request, self.template_name, {'stocks': stock})
