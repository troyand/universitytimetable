from django.db import models


class University(models.Model):
    name = models.CharField(max_length=255, unique=True)
    abbr = models.CharField(max_length=16, unique=True)

    def __unicode__(self):
        return u'%s' % (
                self.abbr
                )


class Faculty(models.Model):
    university = models.ForeignKey(University)
    name = models.CharField(max_length=255)
    abbr = models.CharField(max_length=16)

    class Meta:
        unique_together = (
                ('university', 'name'),
                ('university', 'abbr'),
                )

    def __unicode__(self):
        return '%s - %s' % (
                self.university.abbr,
                self.abbr,
                )
