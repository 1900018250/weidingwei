from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.generic.base import View
from .models import User, Item, Result
from .form import UserForm, ItemListForm,ItemForm, ResultForm
from .tool import get_error_json, get_data_json, CreatePage


class UserView(View):
    def get(self, request):
        # 获取用户信息
        openid = request.GET.get('openid', '')
        all_user = User.objects.filter(openid=openid)
        if all_user:
            return HttpResponse(get_data_json(all_user), content_type='application/json')
        return HttpResponseBadRequest('{"status":"error", "error":1001, "msg":"不存在此openid"}',
                                      content_type='application/json')

    def put(self, request):
        # 更新用户信息
        active_form = UserForm(request.PUT)
        if active_form.is_valid():  # 验证提交的数据
            openid = request.PUT.get('openid', '')
            all_user = User.objects.filter(openid=openid)
            if all_user:    # 判断是否存在这个用户信息
                for user in all_user:
                    user.email = request.PUT.get('email', '')
                    user.phone = request.PUT.get('phone', '')
                    user.is_email = int(request.PUT.get('isEmail', 0))
                    user.is_phone = int(request.PUT.get('isPhone', 0))
                    user.save()
                    return HttpResponse('{"status":"success"}', content_type='application/json')
            return HttpResponseBadRequest('{"status":"error", "error":1001, "msg":"不存在此openid"}',
                                          content_type='application/json')
        return HttpResponseBadRequest(get_error_json(active_form), content_type='application/json')

    def post(self, request):
        # 增加用户
        active_form = UserForm(request.POST)
        if active_form.is_valid():      # 验证提交的数据
            openid = request.POST.get('openid', '')
            # 判断 openid 是否存在
            user = User.objects.filter(openid=openid)
            if user:    # 如果已存在返回1002错误
                return HttpResponseBadRequest('{"status":"error", "error":1002, "msg":"此openid已存在"}',
                                              content_type='application/json')
            else:
                email = request.POST.get('email', '')
                phone = request.POST.get('phone', '')
                is_email = int(request.POST.get('isEmail', 0))
                is_phone = int(request.POST.get('isPhone', 0))
                User.objects.create(openid=openid, email=email, phone=phone, is_email=is_email, is_phone=is_phone)
                return HttpResponse('{"status":"success"}', content_type='application/json')
        return HttpResponseBadRequest(get_error_json(active_form), content_type='application/json')


class ItemListView(View):
    def get(self, request):
        # 获取用户的定位item列表
        openid = request.GET.get('openid', '')
        item_list = Item.objects.filter(user__openid=openid)
        return HttpResponse(get_data_json(item_list, False), content_type='application/json')

    def post(self, request):
        # 添加定位item
        active_form = ItemListForm(request.POST)
        if active_form.is_valid():
            random_str = CreatePage.get_random_str()
            pro_link = 'http://wdw.summeroo.club/dw/{0}/'.format(random_str)
            openid = request.POST.get('openid', '')
            user = User.objects.get(openid=openid)
            title = request.POST.get('title', '')
            name = request.POST.get('name', '')
            link = request.POST.get('link', '')
            details = request.POST.get('details', '')
            itemid = Item.objects.create(user=user, pro_link=pro_link, title=title, name=name, link=link,
                                         details=details)
            CreatePage.render_page(openid, str(itemid), link, random_str)
            return HttpResponse('{"status":"success"}', content_type='application/json')
        return HttpResponseBadRequest(get_error_json(active_form), content_type='application/json')


class ItemView(View):
    def get(self, request):
        # 获取定位item详细信息
        openid = request.GET.get('openid', '')
        itemid = request.GET.get('itemid', '')
        if not itemid: itemid = -1       # 如果没有传id默认为-1
        item = Item.objects.filter(user__openid=openid, id=int(itemid))
        if item:
            return HttpResponse(get_data_json(item), content_type='application/json')
        return HttpResponseBadRequest('{"status":"error", "error":1001, "msg":"没有数据"}',
                                      content_type='application/json')

    def put(self, request):
        # 修改定位item的信息
        active_form = ItemForm(request.PUT)
        if active_form.is_valid():
            openid = request.PUT.get('openid', '')
            itemid = request.PUT.get('itemid', '')
            all_item = Item.objects.filter(user__openid=openid, id=int(itemid))
            if not all_item:
                return HttpResponseBadRequest('{"status":"error", "error":1001, "msg":"没有此条记录"}',
                                              content_type='application/json')
            for item in all_item:
                item.title = request.PUT.get('title', '')
                item.name = request.PUT.get('name', '')
                item.link = request.PUT.get('link', '')
                item.details = request.PUT.get('details', '')
                item.save()
                return HttpResponse('{"status":"success"}', content_type='application/json')
        return HttpResponseBadRequest(get_error_json(active_form), content_type='application/json')

    def delete(self, request):
        # 删除定位item
        openid = request.DELETE.get('openid', '')
        itemid = request.DELETE.get('itemid', '')
        item_all = Item.objects.filter(user__openid=openid, id=int(itemid))
        if item_all:
            item_all.delete()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponseBadRequest('{"status":"error", "error":1001, "msg":"没有此条记录"}',
                                          content_type='application/json')


class ResultListView(View):
    def get(self, request):
        # 获取该openid 该 item下的定位结果
        openid = request.GET.get('openid', '')
        itemid = request.GET.get('itemid', '')
        result_list = Result.objects.filter(user__openid=openid, item__id=int(itemid))
        if result_list:
            return HttpResponse(get_data_json(result_list, False), content_type='application/json')
        return HttpResponseBadRequest('{"status":"error", "error":1001, "msg":"没有数据"}',
                                      content_type='application/json')

    def post(self, request):
        # 添加定位结果
        active_form = ResultForm(request.POST)
        if active_form.is_valid():
            openid = request.POST.get('openid', '')
            itemid = request.POST.get('itemid', '')
            user = User.objects.filter(openid=openid)
            item = Item.objects.filter(user__openid=openid, id=int(itemid))
            if user and item:   # 如果存在这个openid和存在这个定位item
                flag = request.POST.get('flag', '')
                ip = request.POST.get('ip', '')
                lng = request.POST.get('lng', '')
                lat = request.POST.get('lat', '')
                address = request.POST.get('address', '')
                Result.objects.create(user=user[0], item=item[0], flag=int(flag), ip=ip, lng=lng, lat=lat, address=address)
                return HttpResponse('{"status":"success"}', content_type='application/json')
            else:
               return HttpResponseBadRequest('{"status":"error", "error":1001, "msg":"没有此用户或定位"}',
                                             content_type='application/json')
        return HttpResponseBadRequest(get_error_json(active_form), content_type='application/json')


class ResultView(View):
    def get(self, request):
        openid = request.GET.get('openid', '')
        itemid = request.GET.get('itemid', '')
        resultid = request.GET.get('resultid', '')
        result = Result.objects.filter(user__openid=openid, item__id=int(itemid), id=int(resultid))
        if result:
            return HttpResponse(get_data_json(result), content_type='application/json')
        return HttpResponseBadRequest('{"status":"error", "error":1001, "msg":"没有此数据"}',
                                      content_type='application/json')
