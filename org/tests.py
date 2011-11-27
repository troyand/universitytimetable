#-*- coding: utf-8 -*-

from django.test import TestCase
from universitytimetable.org.models import *


class UniversityTest(TestCase):
    def setUp(self):
        University.objects.create(
                name=u'Київський національний університет культури і мистецтв',
                abbr=u'КНУКіМ',
                )

    def test_unicode(self):
        u = University.objects.get(abbr=u'КНУКіМ')
        self.assertEqual(
                u'%s' % u,
                u'КНУКіМ'
                )

    def test_natural_key(self):
        u = University.objects.get(abbr=u'КНУКіМ')
        self.assertEqual(u.natural_key(), (u'КНУКіМ',))


    def tearDown(self):
        u = University.objects.get(abbr=u'КНУКіМ')
        u.delete()


class FacultyTest(TestCase):
    def setUp(self):
        u = University.objects.create(
                name=u'Київський національний університет культури і мистецтв',
                abbr=u'КНУКіМ',
                )
        f = Faculty.objects.create(
                university=u,
                name=u'Факультет індустрії моди',
                abbr=u'ФІМ',
                )

    def test_unicode(self):
        f = Faculty.objects.get(abbr=u'ФІМ')
        self.assertEqual(
                u'%s' % f,
                u'КНУКіМ - ФІМ'
                )

    def test_natural_key(self):
        f = Faculty.objects.get(abbr=u'ФІМ')
        self.assertEqual(f.natural_key(), (u'КНУКіМ', u'ФІМ'))


    def tearDown(self):
        u = University.objects.get(abbr=u'КНУКіМ')
        f = Faculty.objects.get(abbr=u'ФІМ')
        f.delete()
        u.delete()


class MajorTest(TestCase):
    def setUp(self):
        u = University.objects.create(
                name=u'Київський національний університет культури і мистецтв',
                abbr=u'КНУКіМ',
                )
        f = Faculty.objects.create(
                university=u,
                name=u'Факультет індустрії моди',
                abbr=u'ФІМ',
                )
        m = Major.objects.create(
                faculty=f,
                code=u'6.07770777',
                name=u'Дизайн зачіски',
                kind=u'бакалавр',
                )

    def test_unicode(self):
        m = Major.objects.get(code=u'6.07770777')
        self.assertEqual(
                u'%s' % m,
                u'6.07770777 - Дизайн зачіски'
                )

    def tearDown(self):
        u = University.objects.get(abbr=u'КНУКіМ')
        f = Faculty.objects.get(abbr=u'ФІМ')
        m = Major.objects.get(code=u'6.07770777')
        m.delete()
        f.delete()
        u.delete()


class DepartmentTest(TestCase):
    def setUp(self):
        u = University.objects.create(
                name=u'Київський національний університет культури і мистецтв',
                abbr=u'КНУКіМ',
                )
        f = Faculty.objects.create(
                university=u,
                name=u'Факультет індустрії моди',
                abbr=u'ФІМ',
                )

    def test_unicode(self):
        f = Faculty.objects.get(abbr=u'ФІМ')
        d = Department.objects.create(
                university=None,
                faculty=f,
                name=u'Кафедра модного вироку',
                )
        self.assertEqual(
                u'%s' % d,
                u'Кафедра модного вироку'
                )

    def test_validation_fail1(self):
        from django.db import IntegrityError
        with self.assertRaises(IntegrityError):
            d = Department.objects.create(
                    university=None,
                    faculty=None,
                    name=u'Кафедра модного вироку',
                    )

    def test_validation_fail2(self):
        from django.db import IntegrityError
        with self.assertRaises(IntegrityError):
            f = Faculty.objects.get(abbr=u'ФІМ')
            d = Department.objects.create(
                    university=f.university,
                    faculty=f,
                    name=u'Кафедра модного вироку',
                    )

    def test_validation_success1(self):
        f = Faculty.objects.get(abbr=u'ФІМ')
        d = Department.objects.create(
                university=None,
                faculty=f,
                name=u'Кафедра модного вироку',
                )
        d.delete()

    def test_validation_success2(self):
        u = University.objects.get(abbr=u'КНУКіМ')
        d = Department.objects.create(
                university=u,
                faculty=None,
                name=u'Кафедра модного вироку',
                )
        d.delete()

    def tearDown(self):
        u = University.objects.get(abbr=u'КНУКіМ')
        f = Faculty.objects.get(abbr=u'ФІМ')
        f.delete()
        u.delete()
