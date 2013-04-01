[INF-YTimetab](http://timetab.inf-yt.org.uk)
============================================

INF-YTimetab is the INF-YT's rewrite of the University of
Edinburgh's [Timetab timetabling system](http://www.timetab.ed.ac.uk/).

It produces a standard
[iCal calendar file](http://en.wikipedia.org/wiki/Icalendar)
from a list of your courses, allowing you to import your
lecture timetable into almost any Calendar application, including Google
Calendar, Outlook, and most probably that slide phone you've had since '06.


Querying the Data
-----------------

This application is just an interface to all the magic happening
on the back-end, so getting timetables programmatically is pretty simple.

Just send a [form-encoded](http://www.w3.org/TR/html401/interact/forms#form-data-set) POST request
to the `/timetable` endpoint, with the parameters as `course_codes-n=<course-code>` for each course,
where `n` starts at 0.

You should receive a raw calendar back, with the `content-type` header set to `text/calendar`.

For example, using [httpie](https://github.com/jkbr/httpie):

```bash
>>> http --form POST http://timetab.inf-yt.org.uk/timetable course_codes-0='MATH08058'
# should return something along the lines of:
HTTP/1.1 200 OK
Content-Length: # ...
Content-Type: text/calendar
# [...]

BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
DTSTART;TZID=Europe/London:20130114T121000
DTEND;TZID=Europe/London:20130114T130000
RRULE:FREQ=WEEKLY;UNTIL=20130408T131000Z
UID:MATH08058o12@infyt.raj
DESCRIPTION:
LOCATION:No Location Data Available
SUMMARY:Calculus and its Applications
TRANSP:OPAQUE
END:VEVENT
# [...]
END:VCALENDAR

>>> # and so on...
```


About
-----

INF-YTimetab is one component in the INF-YT's
[ILWHack-winning project](http://data.inf.ed.ac.uk/ilwhack/), illustrating
the awesome crossovers and mashups that could occur if the University opened
up its data sources.

So this is a bit better than an HTML table, non?
