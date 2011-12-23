# -*- coding: utf-8 -*-


import sys
import codecs
import re
import csv

def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),
                            dialect=dialect, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [unicode(cell, 'utf-8') for cell in row]

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')


def parse_line(day, lesson_time, weeks, text, group, room):
    try:
        discipline, lecturer = re.split(
                r'[ ]+-[ ]*',
                text)
        statuses = [u'ст. викл.', u'доц.', u'проф.']
        status = '?'
        name = lecturer
        for s in statuses:
            if lecturer.startswith(s):
                status = s
                name = lecturer.replace(s+' ', '')

        return day, lesson_time, status, name, discipline, weeks
    except ValueError:
        try:
            discipline, lecturer = re.split(
                    r'[ ]*-[ ]*',
                    text)
        except ValueError:
            print text.rjust(80)

def sanitize(row):
    result = []
    for s in row:
        # change "." => ". " if s does not start with digit and len(s) != 0
        if len(s) and s[0] not in '0123456789':
            s = s.replace('.', '. ')
        # change "  " => " "
        s = s.replace('  ', ' ')
        # change "--" => "-"
        s = s.replace('--', '-')
        result.append(s)
    return result

def main(filename):
    previous = None
    #for line in codecs.open(filename, 'r', 'utf8'):
    reader = unicode_csv_reader(codecs.open(filename, 'r', 'utf-8'))
    # skip the until the header
    while reader.next()[0] != u'День':
        pass
    # skip one more line
    names = set()
    disciplines = set()
    reader.next()
    prev_day = None
    prev_lesson_time = None
    for row in reader:
        row = sanitize(row)
        day, lesson_time, weeks, text, group, room = row[:6]
        if day:
            prev_day = day
        else:
            day = prev_day
        if lesson_time:
            prev_lesson_time = lesson_time
        else:
            lesson_time = prev_lesson_time
        if weeks or lesson_time.startswith(u'Провідний'):
            # if weeks text is present, we then the previous line is complete
            # and it is ready to be parsed
            if previous:
                try:
                    day, lesson_time, status, name, discipline, weeks = parse_line(*previous)
                    names.add(name)
                    disciplines.add(discipline)
                except TypeError:
                    pass
            if lesson_time.startswith(u'Провідний'):
                break
            previous = [day, lesson_time, weeks, text, group, room]
        else:
            previous[3] += text
    print '\n'.join(disciplines)
    print '\n'.join(names)




if __name__ == '__main__':
    main(sys.argv[1])
