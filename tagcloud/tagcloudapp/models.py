from django.db import models

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

class Tag(models.Model):
    tagvalue = models.CharField(max_length=100, null=True)
    tagsize = models.IntegerField(default=1, null=True)
        
    class Meta:
        db_table = "tag"
    
    def __str__(self):
        return self.tagvalue

# user_has_subjects = db.Table('user_has_subjects',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#     db.Column('subject_id', db.Integer, db.ForeignKey('subject.id'))
# )

class Subject(models.Model):
    name = models.CharField(max_length=45)
    descr = models.CharField(max_length=400, null=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
    workpackage = models.ForeignKey(Workpackage, on_delete=models.CASCADE, null=True)
    tag = models.ManyToManyField(Tag, related_name='subjects')
     
    class Meta:
        db_table = "subject"
    
    def __str__(self):
        return self.name

# subject_has_tags = db.Table('subject_has_tags',
#     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
#     db.Column('subject_id', db.Integer, db.ForeignKey('subject.id'))
# )

# user_has_tags = db.Table('user_has_tags',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
# )