from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Tag, Subject, Project, Workpackage, TagSubmitHistory, SubjectTags

class ProjectForm(forms.ModelForm):
    descr = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    class Meta:
        model = Project
        fields = ('__all__')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id','name','descr','start','end')
    list_display_links = ('id','name','descr','start','end')
    form = ProjectForm

class WorkpackageForm(forms.ModelForm):
    descr = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    class Meta:
        model = Workpackage
        fields = ('__all__')

class WorkpackageAdmin(admin.ModelAdmin):
    list_display = ('id','name','descr','start','end','project')
    list_display_links = ('id','name','descr','start','end','project')
    list_filter = ('project',)
    form = WorkpackageForm

class SubjectForm(forms.ModelForm):
    descr = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
    class Meta:
        model = Subject
        fields = ('__all__')

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id','name','descr','start','end','workpackage')
    list_display_links = ('id','name','descr','start','end','workpackage')
    list_filter = ('workpackage',)
    form = SubjectForm

class TagAdmin(admin.ModelAdmin):
    list_display = ('tagvalue','tagsize','created_on','created_by')
    list_display_links = ('tagvalue','tagsize','created_on','created_by')

class TSHAdmin(admin.ModelAdmin):
    list_display = ('id','tag','first_name_and_last_name','submitted_on')
    list_display_links = ('id','tag','first_name_and_last_name',)
    list_filter = ('user',)
    class Meta:
        model = TagSubmitHistory
        fields = ('__all__')

    def first_name_and_last_name(self, obj):
        return obj.user.first_name+" "+obj.user.last_name
    
    first_name_and_last_name.short_description = "User"
    first_name_and_last_name.admin_order_field = 'user'
    first_name_and_last_name.admin_filter_field = 'user'

class SubjectsTagsAdmin(admin.ModelAdmin):
    list_display = ('id','tag','subject')
    list_display_links = ('id','tag','subject')
    list_filter = ('subject',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Workpackage, WorkpackageAdmin)
admin.site.register(TagSubmitHistory, TSHAdmin)
admin.site.register(SubjectTags, SubjectsTagsAdmin)
