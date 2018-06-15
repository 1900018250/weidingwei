# Generated by Django 2.0.5 on 2018-05-27 06:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='定位名称')),
                ('name', models.CharField(max_length=50, verbose_name='连接名称')),
                ('link', models.CharField(max_length=100, verbose_name='连接地址')),
                ('details', models.CharField(max_length=100, verbose_name='连接描述')),
                ('add_time', models.DateTimeField(default=datetime.datetime(2018, 5, 27, 14, 33, 32, 289980), verbose_name='添加时间')),
                ('update_time', models.DateTimeField(blank=True, null=True, verbose_name='最后更新时间')),
            ],
            options={
                'verbose_name': '定位item信息',
                'verbose_name_plural': '定位item信息',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flag', models.BooleanField(verbose_name='定位是否成功')),
                ('ip', models.CharField(max_length=50, verbose_name='定位ip')),
                ('lng', models.CharField(max_length=10, verbose_name='经度')),
                ('lat', models.CharField(max_length=10, verbose_name='纬度')),
                ('address', models.CharField(max_length=100, verbose_name='地址')),
                ('add_time', models.DateTimeField(default=datetime.datetime(2018, 5, 27, 14, 33, 32, 290482), verbose_name='添加时间')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Item', verbose_name='所属定位item')),
            ],
            options={
                'verbose_name': '定位结果信息',
                'verbose_name_plural': '定位结果信息',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=50, verbose_name='微信openid')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='邮箱')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='手机号码')),
                ('is_email', models.BooleanField(default=False, verbose_name='是否开启邮箱提醒')),
                ('is_phone', models.BooleanField(default=False, verbose_name='是否短信提醒')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
        migrations.AddField(
            model_name='result',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User', verbose_name='所属用户'),
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.User', verbose_name='所属用户'),
        ),
    ]
