from django.contrib import admin
from .models import Tag, Subject, Workpackage
# Register your models here.

admin.site.register(Tag)
admin.site.register(Subject)
admin.site.register(Workpackage)