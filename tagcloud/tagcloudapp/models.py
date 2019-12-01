from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=45)
    descr = models.CharField(max_length=400, null=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "project"

    def __str__(self):
        return self.name

class Workpackage(models.Model):
    name = models.CharField(max_length=45)
    descr = models.CharField(max_length=400, null=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table = "workpackage"
    
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=45)
    descr = models.CharField(max_length=400, null=True, blank=True)
    start = models.DateField(null=True, blank=True)
    end = models.DateField(null=True, blank=True)
    workpackage = models.ForeignKey(Workpackage, on_delete=models.CASCADE, null=True)
     
    class Meta:
        db_table = "subject"
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    tagvalue = models.CharField(max_length=100, null=True)
    tagsize = models.IntegerField(default=1, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    subjects = models.ManyToManyField(Subject, related_name='tags', blank=True)
    created_by = models.ForeignKey(User, related_name='tags_created', on_delete=models.CASCADE, null=True, blank=True)
    usersubmits = models.ManyToManyField(User, related_name='tags_submitted', through='TagSubmitHistory')
        
    class Meta:
        db_table = "tag"
    
    def __str__(self):
        return self.tagvalue

class TagSubmitHistory(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tagsubmithistory"
    
    def __str__(self):
        return self.id, self.tag.tagvalue, self.user.username, self.submitted_on