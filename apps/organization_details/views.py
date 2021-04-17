from django.shortcuts import render
from django.views import View
from django.shortcuts import HttpResponse
from logs.log import *
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .forms import ContactForm
from django.contrib import messages


class IndexView(View):
    """To see desired dates log"""
    template_name = "index.html"

    def get(self, request):
        # Cover photo
        cover = CoverPhoto.objects.filter(is_active=True).order_by('position')

        #

        data = {
            "cover": cover,

        }

        # logger
        Log.info("Successfully send.", request)
        return render(request, self.template_name, context=data)


class ContactView(View):
    """To see desired dates log"""
    template_name = "contact.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.add_message(request, messages.SUCCESS, "Your message sent successfully.")
            return render(request, "contact.html")
        else:
            messages.add_message(request, messages.ERROR, "Couldn't send message. Check all the field carefully.")
            return render(request, "contact.html")


    # def error404(request):
    #     return render(request, '404.html', status=404)
