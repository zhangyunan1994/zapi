from django.db import models

# Create your models here.


class Team(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=40)
    remark = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team'