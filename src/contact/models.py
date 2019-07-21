from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    username = models.CharField(max_length=25, unique=True)
    first_name = models.CharField(db_column='first_name', max_length=50, blank=False, null=False)
    last_name = models.CharField(db_column='last_name', max_length=50, blank=False, null=False)   
    position = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=255,blank=True, null=True)
    executive = models.IntegerField(blank=True, null=True)
    executive_assistant = models.IntegerField( blank=True, null=True)
    phone = models.CharField(db_column='phone', max_length=25, blank=True, null=True)
    email = models.EmailField(null=True, max_length=50, unique=True)
    supports = models.CharField(blank=True, null=True, max_length=100)
    supported_by = models.CharField(db_column='supported_by', blank=True, null=True, max_length=100)
    space_available = models.CharField(db_column='space_available', blank=True, null=True, max_length=255)
    committee = models.CharField(blank=True, null=True, max_length=100)
    notes = models.TextField(blank=True, null=True, max_length=500)
    active = models.IntegerField(blank=True, null=True)
    office_location = models.TextField(db_column='office_location', blank=True, null=True, max_length=255)
    admin = models.IntegerField(db_column='admin', blank=True, null=True)
    
    def __unicode__(self):
        return self.last_name

    class Meta:
        managed = True
        db_table = 'users'
        app_label = 'contact'