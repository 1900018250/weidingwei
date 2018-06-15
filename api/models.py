from datetime import datetime
from django.db import models


# 用户信息
class User(models.Model):
    openid = models.CharField(max_length=50, verbose_name=u'微信openid')
    email = models.CharField(max_length=50, null=True, blank=True, verbose_name=u'邮箱')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name=u'手机号码')
    is_email = models.BooleanField(default=False, verbose_name=u'是否开启邮箱提醒')
    is_phone = models.BooleanField(default=False, verbose_name=u'是否短信提醒')

    # meta信息 后台栏目名
    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.openid


# 定位item信息
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u'所属用户')
    title = models.CharField(max_length=50, verbose_name=u'定位名称')
    name = models.CharField(max_length=50, verbose_name=u'连接名称')
    link = models.CharField(max_length=200, verbose_name=u'连接地址')
    pro_link = models.CharField(null=True, blank=True, max_length=200, verbose_name=u'定位连接地址')
    details = models.CharField(max_length=100, verbose_name=u'连接描述')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    update_time = models.DateTimeField(null=True, blank=True, verbose_name=u'最后更新时间')

    class Meta:
        verbose_name = u'定位item信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}'.format(self.id)


# 定位结果信息
class Result(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u'所属用户')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name=u'所属定位item')
    flag = models.BooleanField(verbose_name=u'定位是否成功')
    ip = models.CharField(max_length=50, verbose_name=u'定位ip')
    lng = models.CharField(max_length=50, verbose_name=u'经度')
    lat = models.CharField(max_length=50, verbose_name=u'纬度')
    address = models.CharField(max_length=200, verbose_name=u'地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'定位结果信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0} ==>> {1} ==> {2}'.format(self.user, self.item, self.address)
