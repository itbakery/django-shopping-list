from django.db import models

class ListItem(models.Model):
    listitem = models.CharField(max_length=60)
    purchased = models.BooleanField()
    def __unicode__(self):
        return self.listitem

