from django.shortcuts import render
from django.views import View
from django.shortcuts import HttpResponse
from logs.log import *
from django.views.generic import ListView,DetailView


class IndexView(View):
    """To see desired dates log"""
    template_name = "index.html"

    def get(self, request):
        #logger
        Log.info("Successfully send.",request)
        return render(request, self.template_name)


class ContactView(View):
    """To see desired dates log"""
    template_name = "contact.html"

    def get(self, request):
        return render(request, self.template_name)


def error404(request):
    return render(request,'404.html', status=404)