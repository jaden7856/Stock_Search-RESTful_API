from django.shortcuts import render

from django.views.generic import ListView, DetailView

from stock.models import Post


class StockLV(ListView):
    model = Post
    template_name = "stock/stock_search.html"

    def stock_db(self, request):
        stock = Post.objects.all().order_by('-id')[0]
        template = 'stock/stock_search.html'
        context = {'stocks': stock, }

        return render(self.request, template, context)


class StockDV(DetailView):
    model = Post

