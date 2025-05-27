from flask_restx import fields
from .extensions import api


student_model = api.model("Student", {
    "id": fields.Integer,
    "name": fields.String
    #"course": fields.Nested(course_model)
})
course_model = api.model("Course", {
    "id": fields.Integer,
    "name": fields.String,
    "students": fields.List(fields.Nested(student_model))
})

cource_input_model = api.model("CourseInput", {
    "name": fields.String(required=True, description="The name of the course")
})

student_input_model = api.model("CourseInput", {
    "name": fields.String(required=True, description="The name of the course"),
    "course_id": fields.Integer(required=True, description="The ID of the course for the student")
})