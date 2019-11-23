import json
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render
from .models import Project, Workpackage, Subject, Tag

# Create your views here.
def tagserfassen(request):
    projects = {
        "projects": Project.objects.all()
    }
    return render(request, "tagserfassen.html", projects)

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

def tagsubmit(request):
    data = json.loads(request.body)
    sub = Subject.objects.get(id=data['selectval']['subid'])
    for x in data['tags']:
        tag = Tag.objects.create(tagvalue=x['value'])
        sub.tag.add(tag)
    return JsonResponse({"Back to JS!": "Back to JS!"})

def tagcloudchart(request):
    projects = {
        "projects": Project.objects.all()
    }
    return render(request, "tagcloudchart.html", projects)

def tagquery(request):
    tclist = []
    id = json.loads(request.body)
    if ('prid' in id):
        tags = Tag.objects.filter(subjects__workpackage__project=id['prid'])
    elif ('wpid' in id):
        tags = Tag.objects.filter(subjects__workpackage=id['wpid'])
    else:
        tags = Tag.objects.filter(subjects=id['subid'])
    for tag in tags:
        tagsdict = {
            'id': tag.id,
            'tagvalue': tag.tagvalue,
            'tagsize': tag.tagsize
        }
        tclist.append(tagsdict)
    return JsonResponse ({'tags': tclist})