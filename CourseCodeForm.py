#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wtforms import Form, TextField, validators, FieldList, SubmitField


class CourseCodeForm(Form):
    """
    Class for holding the given course codes.
    """

    course_codes = FieldList(TextField(
        label='course-code',
        validators=[validators.Regexp('[\w]{4}[\d]{5}')]),
        min_entries=1
    )

    submit_button = SubmitField('Generate Calendar')
