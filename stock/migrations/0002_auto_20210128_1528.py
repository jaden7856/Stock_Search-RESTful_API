# Generated by Django 3.0.6 on 2021-01-28 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='modify_date',
            field=models.CharField(max_length=50, verbose_name='Modify Date'),
        ),
        migrations.AlterModelTable(
            name='post',
            table='blog_post',
        ),
    ]