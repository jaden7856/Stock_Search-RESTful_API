from django.shortcuts import render

from django.views.generic import ListView, DetailView

from stock.models import Post


class StockLV(ListView):
    model = Post
    template_name = "stock/stock_search.html"


class StockDV(DetailView):
    model = Post

