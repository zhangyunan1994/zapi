from django.db import models

# Create your models here.
from team.models import Department, Member


class Project(models.Model):
    name = models.CharField(max_length=30)
    manager = models.ForeignKey(Member, models.DO_NOTHING, blank=True, null=True)
    version = models.CharField(max_length=30, blank=True, null=True)
    department = models.ForeignKey(Department, models.DO_NOTHING)
    remark = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True, default=0)
    create_time = models.DateTimeField()
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'

