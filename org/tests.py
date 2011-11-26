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
