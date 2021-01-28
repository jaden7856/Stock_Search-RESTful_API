from django.contrib import admin
from stock.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'name', 'price', 'open', 'day_min', 'day_max', 'volume', 'modify_date')
    search_fields = ('symbol', 'name')


admin.site.register(Post, PostAdmin)
