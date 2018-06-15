from django.shortcuts import render
from django.views.generic.base import View
from django.http import Http404
# Create your views here.


class RenderHtmlView(View):
    def get(self, request, html):
        html_list = ['help', 'index', 'itemdetails', 'itemresult', 'resultdetails', 'user']
        if not (html in html_list):
            raise Http404("没有这个页面")
        temp = 'm/{0}.html'.format(html)
        return render(request, temp)
