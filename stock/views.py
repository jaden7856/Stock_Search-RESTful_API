from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from stock.models import Post


class StockLV(ListView):
    model = Post
    template_name = "stock/stock_search.html"


def stockDB(request):
    stock = Post.objects.all().order_by('-id')
    context = {'stocks': stock}

    return render(request, 'stock/stock_search.html', context)


class StockDV(DetailView):
    model = Post
    template_name = "stock/stock_detail.html"

    @method_decorator(csrf_exempt)
    def stockDB_detail(request):
        name = request.POST.get('name')
        print(name)
        stock = Post.objects.get(name=name)
        context = {'stocks': stock}

        return render(request, 'stock/stock_detail.html', context)
