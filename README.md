INF-YTimetab
============

INF-YTimetab is the Informatics Young Team's rewrite of the University of
Edinburgh's [Timetab timetabling system](http://www.timetab.ed.ac.uk/).

It produces a standard
[iCal calendar file](http://en.wikipedia.org/wiki/Icalendar)
from a list of your courses, allowing you to import your
lecture timetable into almost any Calendar application, including Google
Calendar, Outlook, and most probably that slide phone you've had since '06.


Querying the Data
-----------------

This application is really just an interface to all the magic happening
on the back-end. Because of this, querying the data is simples!

Just send a POST request to the `/timetable` endpoint, with the parameters as `course_codes-n=<course-code>` for each course, where `n`
starts at 0.


About
-----

INF-YTimetab is one component in the Informatics Young Team's
[ILWHack-winning project](http://data.inf.ed.ac.uk/ilwhack/), illustrating
the awesome crossovers and mashups that could occur if the University opened
up its data sources.

So this is a bit better than an HTML table, non?
