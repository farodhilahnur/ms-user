from django.db import models
from django.utils import timezone
import django

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(db_column='name', max_length=1000, blank=True, null=True, verbose_name='Name')
    password = models.CharField(db_column='password', max_length=1000, blank=True, null=True, verbose_name='password')
    createdAt = models.DateTimeField(db_column='createdAt', blank=True, null=True, default=django.utils.timezone.now, verbose_name='Created At')
    createdBy = models.IntegerField(db_column='createdBy', blank=True, null=True,  verbose_name='Created By')
    class Meta:
        db_table = 'user'
    def save(self, *args, **kwargs):
        return super(User, self).save(*args, **kwargs)