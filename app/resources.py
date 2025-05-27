from flask_restx import Resource, Namespace
from .models import Course, Student
from .api_models import *
from .extensions import db

ns = Namespace("api")

@ns.route("/hello")
class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello, World!"}

@ns.route("/courses")
class CourseListAPI(Resource):
    @ns.marshal_list_with(course_model)
    def get(self):
        return Course.query.all()
    
    @ns.expect(cource_input_model)
    @ns.marshal_with(course_model)
    def post(self):
        print(ns.payload)
        course = Course(name=ns.payload["name"])
        db.session.add(course)
        db.session.commit()
        return course, 201
    
@ns.route("/courses/<int:id>")
class CourseIdAPI(Resource):
    @ns.marshal_with(course_model)
    def get(self, id):
        course = Course.query.get_or_404(id)
        return course

@ns.route("/students")
class StudentListAPI(Resource):
    @ns.marshal_list_with(student_model)
    def get(self):
        return Student.query.all()
    
    @ns.expect(student_input_model)
    @ns.marshal_with(student_input_model)
    def post(self):
        print(ns.payload)
        student = Student(name=ns.payload["name"], course_id=ns.payload["course_id"])
        db.session.add(student)
        db.session.commit()
        return student, 201
    
@ns.route("/students/<int:id>")
class StudentAPI(Resource):
    @ns.marshal_with(student_model)
    def get(sefl,id):
        student = Student.query.get_or_404(id)
        return student
    
    @ns.expect(student_input_model)
    @ns.marshal_with(student_model)
    def put(self, id):
        student = Student.query.get_or_404(id)
        student.name = ns.payload["name"]
        student.course_id = ns.payload["course_id"]
        db.session.commit()
        return student, 200
    
    @ns.expect(student_input_model)
    @ns.marshal_with(student_model)
    def patch(self, id):
        student = Student.query.get_or_404(id)
        if "name" in ns.payload:
            student.name = ns.payload["name"]
        if "course_id" in ns.payload:
            student.course_id = ns.payload["course_id"]
        db.session.commit()
        return student, 200

    @ns.response(204, "Student deleted")
    def delete(self, id):
        student = Student.query.get_or_404(id)
        db.session.delete(student)
        db.session.commit()
        return "", 204
    