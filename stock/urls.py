from django.urls import path
from stock.views import StockLV, StockDV, stockDB

app_name = 'stock'

urlpatterns = [
    path('', stockDB, name='stock_list'),
    path('detail', StockDV.stockDB_detail, name='stock_detail'),
]