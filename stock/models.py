from django.db import models


class Post(models.Model):
    objects = models.Manager()

    symbol = models.CharField('SYMBOL', unique=True, max_length=50)
    name = models.CharField('NAME', max_length=100)
    price = models.CharField('PRICE', max_length=50)
    open = models.CharField('OPEN', max_length=50)
    day_min = models.CharField('DAY_MIN', max_length=50)
    day_max = models.CharField('DAY_MAX', max_length=50)
    volume = models.CharField('VOLUME', max_length=50)
    modify_date = models.CharField('Modify Date', max_length=50)

    def __str__(self):
        return self.symbol

    class Meta:
        db_table = "blog_post"
