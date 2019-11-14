import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
from .models import Project, Workpackage, Subject

# Create your views here.
def index(request):
    projects = {
        "projects": Project.objects.all()
    }
    return render(request, "index.html", projects)

def projectselect(request):
    wplist = []
    prid = json.loads(request.body)
    wp = Workpackage.objects.filter(project=prid['prid'])
    for x in wp:
        wpdict = {
            'id': x.id,
            'name': x.name
        }
        wplist.append(wpdict)
    return JsonResponse({'wps' : wplist})

def wpselect(request):
    sublist = []
    wpid = json.loads(request.body)
    sub = Subject.objects.filter(workpackage=wpid['wpid'])
    for x in sub:
        subdict = {
            'id': x.id,
            'name': x.name
        }
        sublist.append(subdict)
    return JsonResponse({'subs' : sublist})
