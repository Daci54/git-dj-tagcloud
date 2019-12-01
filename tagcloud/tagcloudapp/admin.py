from django.contrib import admin
from .models import Tag, Subject, Workpackage, TagSubmitHistory
# Register your models here.

admin.site.register(Tag)
admin.site.register(Subject)
admin.site.register(Workpackage)
admin.site.register(TagSubmitHistory)