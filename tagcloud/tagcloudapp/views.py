import json
from django.db.models import F
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from .models import Project, Workpackage, Subject, Tag
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.utils import six 

# Create your views here.
def queryProject():
    projects = {
        "projects": Project.objects.all()
    }
    return projects

def selectSerializer(collection):
    somelist = []
    for something in collection:
        somedict = {
            'id': something.id,
            'name': something.name
        }
        somelist.append(somedict)
    return somelist

def tagSerializer(tags):
    tlist = []
    for tag in tags:
        tagsdict = {
            'id': tag.id,
            'value': tag.tagvalue,
            'tagsize': tag.tagsize
        }
        tlist.append(tagsdict)
    return tlist

def selectquery(request):
    selid = request.POST
    if 'prid' in selid:
        wp = Workpackage.objects.filter(project=selid.get('prid'))
        return JsonResponse({'selval': selectSerializer(wp)})
    else:
        sub = Subject.objects.filter(workpackage=selid.get('wpid'))
        return JsonResponse({'selval': selectSerializer(sub)})

@login_required
def tagserfassen(request):
    return render(request, "tagserfassen.html", queryProject())

@login_required
@require_http_methods(["POST"])
def tagsubmit(request):
    submitdata = json.loads(request.body)
    sub = Subject.objects.get(id=submitdata['subid'])
    for x in submitdata['tags']:
        if 'id' in x:
            Tag.objects.filter(id=x['id']).update(tagsize=F('tagsize')+1)
        else: 
            tag = Tag.objects.create(tagvalue=x['value'])
            sub.tag.add(tag)
    return HttpResponse("Submit Successful")

@login_required
def tagcloudchart(request):
    return render(request, "tagcloudchart.html", queryProject())

@login_required
@require_http_methods(["POST"])
def tagquery(request):
    data = request.POST
    if 'prid' in data:
        tags = Tag.objects.filter(subjects__workpackage__project=data.get('prid'))
    elif 'wpid' in data:
        tags = Tag.objects.filter(subjects__workpackage=data.get('wpid'))
    elif 'subid' in data:
        tags = Tag.objects.filter(subjects=data.get('subid'))
    else:
        tags = Tag.objects.filter(tagvalue__icontains=data['taginput']).order_by('tagvalue')
    return JsonResponse ({'tags': tagSerializer(tags)})

@require_http_methods(["GET"])
def loginpage(request):
    if request.user.is_authenticated:
        return redirect("/")
    return render(request, "registration/login.html")

@require_http_methods(["POST"])
def userLogin(request):
    uname = request.POST.get('username')
    pword = request.POST.get('password')
    user = authenticate(request, username=uname, password=pword)
    if user is not None:
        login(request, user)
    messages.error(request, "Bitte überprüfen Sie Ihre eingaben.")
    return redirect('loginpage')

def userLogout(request):
    logout(request)
    storage = messages.get_messages(request)
    storage.used = True
    messages.success(request, "Sie wurden erfolgreich ausgeloggt")
    return redirect('loginpage')
