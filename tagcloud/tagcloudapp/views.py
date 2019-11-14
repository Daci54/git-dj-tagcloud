import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
from .models import Project, Workpackage

# Create your views here.
def index(request):
    projects = {
        "projects": Project.objects.all()
    }
    return render(request, "index.html", projects)

def optionsselect(request):
    wplist = []
    prid = json.loads(request.body)
    wp = Workpackage.objects.filter(project=prid['id'])
    for x in wp:
        wpdict = {
            'id': x.id,
            'name': x.name
        }
        wplist.append(wpdict)
    return JsonResponse({'wps' : wplist})

