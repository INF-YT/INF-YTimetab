#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
from icalendar_generator import main as generate_ical
from CourseCodeForm import CourseCodeForm

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calendar():
    form = CourseCodeForm(request.form)

    if request.method == 'POST':
        print form.course_codes.data
        course_codes = [field for field in form.course_codes.data if field != '']
        ical = generate_ical('static/lectures/', form.course_codes.data, 'str')
        return (ical, 200, {'Content-Type': 'text/calendar'})

    # by default, render the template with the form:
    return render_template('course-code-form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
