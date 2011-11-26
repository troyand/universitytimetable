from django.db import models

class UniversityManager(models.Manager):
    def get_by_natural_key(self, abbr):
        return self.get(abbr=abbr)


class University(models.Model):
    objects = UniversityManager()

    name = models.CharField(max_length=255, unique=True)
    abbr = models.CharField(max_length=16, unique=True)

    def natural_key(self):
        return (
                self.abbr,
                )

    def __unicode__(self):
        return u'%s' % (
                self.abbr
                )


class FacultyManager(models.Manager):
    def get_by_natural_key(self, university_abbr, abbr):
        return self.get(
                university=University.objects.get_by_natural_key(
                    university_abbr
                    ),
                abbr=abbr
                )


class Faculty(models.Model):
    objects = FacultyManager()

    university = models.ForeignKey(University)
    name = models.CharField(max_length=255)
    abbr = models.CharField(max_length=16)

    class Meta:
        unique_together = (
                ('university', 'name'),
                ('university', 'abbr'),
                )

    def natural_key(self):
        return (
                self.university.abbr,
                self.abbr,
                )

    def __unicode__(self):
        return '%s - %s' % (
                self.university.abbr,
                self.abbr,
                )


class Major(models.Model):
    faculty = models.ForeignKey(Faculty)
    code = models.CharField(max_length=64)
    name = models.CharField(max_length=255)
    kind = models.CharField(max_length=16)

    class Meta:
        unique_together = ('faculty', 'name', 'kind')

    def __unicode__(self):
        return u'%s - %s' % (
                self.code,
                self.name,
                )

