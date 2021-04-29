from django.shortcuts import render
from django.views import View
from django.shortcuts import HttpResponse
from logs.log import *
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from apps.organization_activity.models import ProjectsGallary
from .forms import ContactForm
from django.contrib import messages
from utils.email_services import EMAIL


class IndexView(View):
    """To see desired dates log"""
    template_name = "index.html"

    def get(self, request):
        # Cover photo
        cover = CoverPhoto.objects.filter(is_active=True).order_by('position')
        # Quote
        quote = Quote.objects.filter(will_show_in_homepage=True).order_by('position')
        # Gallery image
        gallery = ProjectsGallary.objects.filter(is_active=True)[:8]

        data = {
            "cover": cover,
            "quote":quote,
            "gallery": gallery

        }

        # logger
        Log.info("Successfully send.", request)
        return render(request, self.template_name, context=data)


class ContactView(View):
    """contact form"""
    template_name = "contact.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save()

            email_service = EMAIL()
            email_service.send_email_service(
                name=form.cleaned_data['name'] ,
                phn=form.cleaned_data['phn'] ,
                subject="Contact from Muslim Aid",
                message=form.cleaned_data['message'],
                recipient_list=[form.cleaned_data['email']]
            )

            messages.add_message(request, messages.SUCCESS, "Your message sent successfully.")
        else:
            messages.add_message(request, messages.ERROR, "Couldn't send message. Check all the field carefully.")
        return render(request, self.template_name)


    # def error404(request):
    #     return render(request, '404.html', status=404)
