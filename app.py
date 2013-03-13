#!/usr/bin/env python
# -*- coding: utf-8 -*-
from CourseCodeForm import CourseCodeForm
from flask import Flask, request, render_template
from icalendar_generator import main as generate_ical
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = CourseCodeForm(request.form)
    return render_template('course-code-form.html', form=form)


@app.route('/timetable', methods=['GET', 'POST'])
def timetable():

    if request.method == 'POST':
        form = CourseCodeForm(request.form)
    if request.method == 'GET':
        form = CourseCodeForm(request.args)

    course_codes = [field for field in form.course_codes.data if (len(field) > 0)]

    if not form.validate() or len(course_codes) == 0:
        return render_template('error-page.html', page_title='400 Bad Reqest', error_message='No valid course-codes entered.'), 400

    try:
        ical = generate_ical('static/lectures/', course_codes, 'str')
    except KeyError, e:
        return render_template('error-page.html', page_title='404 Not Found', error_message=e.message), 404
    except Exception, e:
        raise e

    return (ical, 200, {'Content-Type': 'text/calendar'})


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run(debug=True)
