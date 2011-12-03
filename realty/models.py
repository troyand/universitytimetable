#-*- coding: utf-8 -*-

from django.db import models
from universitytimetable.org.models import University

class Building(models.Model):
    university = models.ForeignKey(University)
    number = models.IntegerField(null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        unique_together = ('university', 'number', 'label')

    def __unicode__(self):
        parts = [self.university.abbr]
        if self.number:
            parts.append(u'Корпус №%d' % self.number)
        if self.label:
            parts.append(self.label)
        return u' - '.join(parts)


class Room(models.Model):
    building = models.ForeignKey(Building)
    number = models.IntegerField(null=True, blank=True)
    label = models.CharField(max_length=255, null=True, blank=True)
    floor = models.IntegerField()

    class Meta:
        unique_together = ('building', 'number', 'label')

    def __unicode__(self):
        #Idendification of room itself
        if self.number:
            room_part = u'%d' % self.number
        else:
            room_part = u''
        if self.label:
            room_part += self.label
        else:
            room_part += u''
        #Identification of building
        if self.building.number:
            building_part = u'%d' % self.building.number
            if self.building.label:
                building_part += u'%s' % self.building.label
        elif self.building.label:
            building_part = self.building.label
        else:
            building_part = u''
        return u'-'.join([
                building_part,
                room_part,
                ])

def load_rooms_from_text(text, university):
    import re
    results = re.findall(u'(\d+)-(\d+)([абв]?)', text)
    for building_number, room_number, room_label in sorted(set(results)):
        building = Building.objects.get(
                university=university,number=int(building_number))
        if building.number == 8 or building.number == 9:
            floor = 1
        else:
            floor = int(room_number[0])
        Room.objects.get_or_create(
                building=building, number=int(room_number),
                label=room_label, floor=floor)
