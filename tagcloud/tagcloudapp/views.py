import json
from django.db.models import F
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.core.serializers import serialize
from django.shortcuts import render, redirect
from .models import Project, Workpackage, Subject, Tag, TagSubmitHistory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.utils import six 


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

@login_required
@require_http_methods(["POST"])
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
    return render(request, "tagserfassen.html", {"projects": Project.objects.all()})

@login_required
@require_http_methods(["POST"])
def tagsubmit(request):
    user = request.user
    submitdata = json.loads(request.body)
    sub = Subject.objects.get(id=submitdata['subid'])
    for x in submitdata['tags']:
        if 'id' in x:
            Tag.objects.filter(id=x['id']).update(tagsize=F('tagsize')+1)
            tag = Tag.objects.get(id=x['id'])
            tag.usersubmits.add(user)
            sub.tags.add(tag)
        else:
            tag = Tag.objects.create(tagvalue=x['value'], created_by=user)
            tag.usersubmits.add(user)
            sub.tags.add(tag)
    return HttpResponse("Submit Successful")

@login_required
def tagcloudchart(request):
    return render(request, "tagcloudchart.html", {'projects': Project.objects.all(), 'persons': User.objects.all()})

@login_required
def rankingchart(request):
    return render(request, "rankingchart.html", {'persons': User.objects.all()})

@login_required
@require_http_methods(["POST"])
def tagcountcreatedquery(request):
    tclist = []
    uid = request.POST.get('uid')
    if uid == "all":
        users = User.objects.all()
        for u in users:
            tcdict = {
                'name': u.first_name+" "+u.last_name,
                'tagcount': Tag.objects.filter(created_by=u.id).count()
            }
            tclist.append(tcdict)
    else:
        u = User.objects.get(id=uid)
        tcdict = {
            'name': u.first_name+" "+u.last_name,
            'tagcount': Tag.objects.filter(created_by=uid).count()
        }
        tclist.append(tcdict)
    return JsonResponse({'tagcount': tclist})

@login_required
@require_http_methods(["POST"])
def tagcountsubmittedquery(request):
    tclist = []
    uid = request.POST.get('uid')
    if uid == "all":
        users = User.objects.all()
        for u in users:
            tcdict = {
                'name': u.first_name+" "+u.last_name,
                'tagcount': u.tags_submitted.all().count()
            }
            tclist.append(tcdict)
    else:
        u = User.objects.get(id=uid)
        tcdict = {
            'name': u.first_name+" "+u.last_name,
            'tagcount': u.tags_submitted.all().count()
        }
        tclist.append(tcdict)
    return JsonResponse({'tagcount': tclist})

@login_required
@require_http_methods(["POST"])
def tagquery(request):
    data = request.POST
    if 'prid' in data:
        tags = Tag.objects.filter(subjects__workpackage__project=data.get('prid')).distinct()
    elif 'wpid' in data:
        tags = Tag.objects.filter(subjects__workpackage=data.get('wpid')).distinct()
    elif 'subid' in data:
        tags = Tag.objects.filter(subjects=data.get('subid'))
    elif 'uid' in data:
        if 'all' in data.get('uid'):
            tags = Tag.objects.all()
        else:
            tags = User.objects.get(id=data.get('uid')).tags_submitted.all()
    else:
        tags = Tag.objects.filter(tagvalue__icontains=data['taginput']).order_by('tagvalue')
    return JsonResponse ({'tags': tagSerializer(tags)})

@require_http_methods(["GET"])
def loginpage(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        return render(request, "registration/login.html")

@require_http_methods(["POST"])
def userLogin(request):
    uname = request.POST.get('username')
    pword = request.POST.get('password')
    user = authenticate(request, username=uname, password=pword)
    if user is not None:
        login(request, user)
        request.session.set_expiry(1800)
    else:
        messages.error(request, "Login fehlgeschlagen: Bitte überprüfen Sie Ihre Eingaben.")
    return redirect('loginpage')

def userLogout(request):
    logout(request)
    storage = messages.get_messages(request)
    storage.used = True
    messages.success(request, "Sie wurden erfolgreich ausgeloggt")
    return redirect('loginpage')
