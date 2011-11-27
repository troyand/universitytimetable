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


class Department(models.Model):
    university = models.ForeignKey(University, null=True, blank=True)
    faculty = models.ForeignKey(Faculty, null=True, blank=True)
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ('university', 'faculty', 'name')

    def clean(self):
        from django.core.exceptions import ValidationError
        # Department should have either university not Null
        # or faculty not Null, not both.
        # In first case the department is university-wide,
        # in the second it is faculty-related
        if self.university is None and self.faculty is not None:
            pass
        elif self.university is not None and self.faculty is None:
            pass
        elif self.university is None and self.faculty is None:
            raise ValidationError(
                    'Either university or faculty should be defined'
                    )
        elif self.university is not None and self.faculty is not None:
            raise ValidationError(
                    'Only one of the following should be defined: university or faculty'
                    )
        else: # pragma: no cover
            pass # this should never happen

    def save(self, *args, **kwargs):
        from django.core.exceptions import ValidationError
        from django.db import IntegrityError
        try:
            self.clean()
        except ValidationError, e:
            raise IntegrityError(e.messages[0])
        super(Department, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
