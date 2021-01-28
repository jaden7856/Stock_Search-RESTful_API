from django.urls import path
from stock.views import StockLV, StockDV

app_name = 'stock'

urlpatterns = [
    path('', StockLV.as_view(), name='stock_list'),
    path('<int:pk>', StockDV.as_view(), name='stock_detail'),
]