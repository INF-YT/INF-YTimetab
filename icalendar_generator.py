#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import os
import os.path
import cStringIO
import sys


def main(event_directory, course_codes, output_file=''):
    """
    Produce an ical calendar containing all the events for the given
    course-code list, using the individual lecture calendars stored in
    the event-directory.
    """
    try:
        course_codes = [field for field in course_codes if (len(field) > 0)]
        if len(course_codes) <= 0:
            raise
    except Exception, e:
        raise ValueError('No valid course codes passed to icalendar_generator: ' + e.message)

    filename_list = []
    for filename in os.listdir(event_directory):
        for code in course_codes:
            if filename.startswith(code):
                filename_list.append(str(os.path.join(event_directory, filename)))

    out = sys.stdout
    if output_file.startswith('str'):
        # write to an internal string object
        out = cStringIO.StringIO()
    elif output_file != '':
        out = open(output_file, 'w')

    out.write("BEGIN:VCALENDAR\nVERSION:2.0\n")

    for filename in filename_list:
        f = open(filename, 'r')
        # remove the first, second, and last lines
        lines = f.readlines()[2:-1]
        for line in lines:
            out.write(line)

    out.write("END:VCALENDAR")

    if output_file.startswith('str'):
        out.seek(0)
        return out.read()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Produce an ical calendar containing all the events for the given course-codes, using the individual lecture events stored in the event-directory.')
    parser.add_argument('-d', '--event-directory', default='lectures',
        help='the directory where ical event files are stored')
    parser.add_argument('course-code', nargs='+',
        help='course codes consisting of 4 letters and 5 numbers, i.e. MATH08058')
    parser.add_argument('-f', '--file', help='output filename')
    args = parser.parse_args()

    event_directory = './static/lectures'
    if args.event_directory:
        event_directory = args.event_directory
    course_codes = vars(args)['course-code']

    main(event_directory, course_codes)
