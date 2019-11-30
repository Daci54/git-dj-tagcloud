import json
from django.db.models import F
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from .models import Project, Workpackage, Subject, Tag
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.http import require_http_methods

# Create your views here.
def queryProject():
    projects = {
        "projects": Project.objects.all()
    }
    return projects

@login_required
def tagserfassen(request):
    return render(request, "tagserfassen.html", queryProject())

@login_required
@require_http_methods(["POST"])
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

@login_required
@require_http_methods(["POST"])
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

@login_required
@require_http_methods(["POST"])
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

@login_required
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

@login_required
@require_http_methods(["POST"])
def tagquery(request):
    data = json.loads(request.body)
    if 'prid' in data:
        tags = Tag.objects.filter(subjects__workpackage__project=data['prid'])
    elif 'wpid' in data:
        tags = Tag.objects.filter(subjects__workpackage=data['wpid'])
    elif 'subid' in data:
        tags = Tag.objects.filter(subjects=data['subid'])
    else:
        tags = Tag.objects.filter(tagvalue__icontains=data['taginput']).order_by('tagvalue')
    return JsonResponse ({'tags': tagfunction(tags)})

@require_http_methods(["GET"])
def loginpage(request):
    if request.user.is_authenticated:
        return redirect("/")
    return render(request, "registration/login.html")

@login_required
@require_http_methods(["POST"])
def test(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        pword = request.POST.get('password')
        user = authenticate(request, username=uname, password=pword)
        if user.is_authenticated:
            login(request, user)
            redirect_url = reverse('tagserfassen')
            return JsonResponse({'url':redirect_url})
        raise PermissionError
    return redirect('loginpage')