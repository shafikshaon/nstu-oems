from django.shortcuts import render

# Create your views here.
from django.views import View


class ProjectDetail(View):
    def get(self, request):
        return render(request, 'project/project-details.html')


class ProjectAllList(View):
    def get(self, request):
        return render(request, 'project/project-all-list.html')
