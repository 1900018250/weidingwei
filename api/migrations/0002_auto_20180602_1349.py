# Generated by Django 2.0.5 on 2018-06-02 13:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='pro_link',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='定位连接地址'),
        ),
        migrations.AlterField(
            model_name='item',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 2, 13, 49, 52, 140341), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='item',
            name='link',
            field=models.CharField(max_length=200, verbose_name='连接地址'),
        ),
        migrations.AlterField(
            model_name='result',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 2, 13, 49, 52, 140341), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='result',
            name='address',
            field=models.CharField(max_length=200, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='result',
            name='lat',
            field=models.CharField(max_length=50, verbose_name='纬度'),
        ),
        migrations.AlterField(
            model_name='result',
            name='lng',
            field=models.CharField(max_length=50, verbose_name='经度'),
        ),
    ]
