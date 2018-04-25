from django.db import models
# Create your models here.


class Api(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    http = models.IntegerField()
    method = models.CharField(max_length=10)
    project_id = models.IntegerField(blank=True, null=True)
    request_params = models.CharField(max_length=500, blank=True, null=True)
    response_params = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'api'


class Environment(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    header = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'environment'
