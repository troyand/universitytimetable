from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=64, null=True, blank=True)
    middle_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)

    def __unicode__(self):
        return u'%s %s.%s.' % (
                self.last_name,
                self.first_name[0],
                self.middle_name[0],
                )
