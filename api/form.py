from .models import User
from django import forms


class UserForm(forms.Form):
    openid = forms.CharField(required=True, max_length=50)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True, max_length=20, min_length=5)
    isEmail = forms.ChoiceField(choices=((0, '关闭'), (1, '开启')))
    isPhone = forms.ChoiceField(choices=((0, '关闭'), (1, '开启')))


class ItemForm(forms.Form):
    openid = forms.CharField(required=True, max_length=50)
    itemid = forms.IntegerField(required=True)
    title = forms.CharField(required=True, max_length=50)
    name = forms.CharField(required=True, max_length=50)
    link = forms.CharField(required=True, max_length=100)
    details = forms.CharField(required=True, max_length=100)


class ItemListForm(ItemForm):
    itemid = forms.IntegerField(required=False)


class ResultForm(forms.Form):
    openid = forms.CharField(required=True, max_length=50)
    itemid = forms.IntegerField(required=True)
    flag = forms.ChoiceField(choices=((0, '成功'), (1, '失败')))
    ip = forms.CharField(required=True, max_length=50,)
    lng = forms.CharField(required=True, max_length=20,)
    lat = forms.CharField(required=True, max_length=20,)
    address = forms.CharField(required=True, max_length=100)

# import re//这个是引用对应的正则验证包
#
# class UserForm(BaseModelForm):
#     phone = forms.CharField(label='手机号码',help_text='（必填）例：13888888888/0771-3236558', required=True,max_length=30,min_length=11)
#     email = forms.EmailField(label='邮箱', help_text='（必填）',required=True,error_messages={'required':"请输入邮箱地址"})
#     class Meta:
#         model = User
#         fields = ['phone', 'email']
#     def clean_phone(self)://clearn_字段名称
#           phone = self.cleaned_data['phone']//获取对应的字段
#           pattern=re.compile(r"^((\d{3,4}-)?\d{7,8})$|(1[3-9][0-9]{9})")//设置正则验证
#           if pattern.match(phone)://如果验证失败的话就会返回none
#              pass
#           else:
#               msg=u"请输入正确的机机或座机号码！"
#               self._errors["phone"] = self.error_class([msg])//设置输入框的告警文字
#           self.phone=phone
#           return phone

