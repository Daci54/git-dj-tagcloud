import json
from django.db.models import F
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render
from .models import Project, Workpackage, Subject, Tag

# Create your views here.
def queryProject():
    projects = {
        "projects": Project.objects.all()
    }
    return projects

def tagserfassen(request):
    return render(request, "tagserfassen.html", queryProject())

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
    sub = Subject.objects.get(id=data['subid'])
    for x in data['tags']:
        if 'id' in x:
            Tag.objects.filter(id=x['id']).update(tagsize=F('tagsize')+1)
        else: 
            tag = Tag.objects.create(tagvalue=x['value'])
            sub.tag.add(tag)
    return HttpResponse("Submit Successful")

def tagcloudchart(request):
    return render(request, "tagcloudchart.html", queryProject())

def tagfunction(tags):
    tlist = []
    for tag in tags:
        tagsdict = {
            'id': tag.id,
            'value': tag.tagvalue,
            'tagsize': tag.tagsize
        }
        tlist.append(tagsdict)
    return tlist

def tagquery(request):
    data = json.loads(request.body)
    if ('prid' in data):
        tags = Tag.objects.filter(subjects__workpackage__project=data['prid'])
    elif ('wpid' in data):
        tags = Tag.objects.filter(subjects__workpackage=data['wpid'])
    elif ('subid' in data):
        tags = Tag.objects.filter(subjects=data['subid'])
    else:
        tags = Tag.objects.filter(tagvalue__icontains=data['taginput']).order_by('tagvalue')
    return JsonResponse ({'tags': tagfunction(tags)})