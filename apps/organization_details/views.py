from django.db.models import Count
from django.shortcuts import render
from django.views import View
from django.shortcuts import HttpResponse
from logs.log import *
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import *
from apps.organization_activity.models import ProjectsGallary, Projects
from apps.accounting.models import DebitRecord
from apps.donation.models import DonationRecord
from apps.blog.models import Articles
from .forms import ContactForm
from django.contrib import messages
from utils.email_services import EMAIL
import json
from django.views.decorators.csrf import csrf_exempt


class IndexView(View):
    """To see desired dates log"""
    template_name = "index.html"

    def get(self, request):
        # Cover photo
        cover = CoverPhoto.objects.filter(is_active=True).order_by('position')
        # Quote
        quote = Quote.objects.filter(will_show_in_homepage=True).order_by('position')[:3]
        # Gallery image
        gallery = ProjectsGallary.objects.filter(is_active=True).only('image', 'short_description')[:8]
        # Projects
        projects = Projects.objects.filter(is_active=True, still_raising_fund=True).order_by("created_at")[:3]
        # Raise_fund
        raise_fund = Projects.objects.filter(is_active=True, still_raising_fund=True,
                                             will_show_front_page=True).order_by("created_at").first()
        # Expense
        expenses = DebitRecord.objects.all().order_by('-id').only('title', 'amount', 'created_at')[:5]
        # Donation
        donations = DonationRecord.objects.select_related('donor').all().order_by('-id').only('donor', 'amount',
                                                                                              'created_at')[:5]
        # Blog
        articles = Articles.objects.all().order_by('-id').only('title', 'category', 'author', 'thumbnail',
                                                               'created_at')[:2]
        # Notice
        notices = Notices.objects.filter(published_date__lte=timezone.now()).order_by('-id').only('title',
                                                                                                  'published_date')[:5]

        data = {
            "cover": cover,
            "quote": quote,
            "gallery": gallery,
            "projects": projects,
            "raise_fund": raise_fund,
            "expenses": expenses,
            "donations": donations,
            "articles": articles,
            "notices": notices

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
                name=form.cleaned_data['name'],
                phn=form.cleaned_data['phn'],
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


class SubscriptionView(View):

    def post(self, request):
        email = request.POST.get('email', None)
        if Subscribers.objects.filter(email=email).exists():
            return HttpResponse("This email already listed.")

        inputToSave = Subscribers.objects.create(
            email=email,
            is_active=True
        )
        inputToSave.save()
        return HttpResponse("Successfully added to our list.")


class NoticeListView(ListView):
    """List view with notice & pagination"""
    model = Notices
    template_name = 'notices.html'
    context_object_name = 'notices'
    fields = ('title', 'details', 'published_date',)
    ordering = '-id'
    paginate_by = 20

    def get_queryset(self):
        return Notices.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(NoticeListView, self).get_context_data(**kwargs)
        notices = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(notices, self.paginate_by)
        try:
            notices = paginator.page(page)
        except PageNotAnInteger:
            notices = paginator.page(1)
        except EmptyPage:
            notices = paginator.page(paginator.num_pages)
        context['notices'] = notices
        return context


class NoticeDetailView(DetailView):
    """Notice details page view"""
    model = Notices
    template_name = 'notice-single.html'
    context_object_name = 'notice'
