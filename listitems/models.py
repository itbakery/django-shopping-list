from django.db import models
from django.contrib.auth.models import User

class ListItem(models.Model):
    listitem = models.CharField(max_length=60)
    purchased = models.BooleanField()
    user = models.ForeignKey(User)
    def __unicode__(self):
        return self.listitem

