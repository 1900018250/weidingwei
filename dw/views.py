from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import Http404
# Create your views here.


class RenderDwView(View):
    def get(self, request, random_str):
        temp = 'dw/{0}.html'.format(random_str)
        return render(request, temp)
