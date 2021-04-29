from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView
from django.views import View
from .models import *
from logs.log import *


class ProjectDetailView(View):
    """Project details page view"""
    template_name = 'full-width.html'

    def get(self, request, pk):
        project = get_object_or_404(Projects, pk=pk)
        project_galary = ProjectsGallary.objects.filter(project=project).order_by('id')[:4]

        data = {
            "project":project,
            "project_galary":project_galary
        }
        # logger
        Log.info("Successfully send.", request)
        return render(request, self.template_name, context=data)