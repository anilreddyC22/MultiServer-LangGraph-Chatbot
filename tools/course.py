import requests
from langchain.tools import tool
from config.settings import COURSE_SERVICE


@tool
def get_courses_by_student_id(student_id: int) -> str:
    """
    Fetch all courses for a given student ID.
    """
    try:
        response = requests.get(f"{COURSE_SERVICE}/students/{student_id}/courses")
        response.raise_for_status()
        courses = response.json()
        if not courses:
            return f"No courses found for student {student_id}."
        names = [c['name'] if isinstance(c, dict) and 'name' in c else str(c) for c in courses]
        return f"Courses for student {student_id}: {', '.join(names)}"
    except requests.RequestException as e:
        return f"Error fetching courses for student {student_id}: {str(e)}"

@tool
def get_all_courses_with_students() -> str:
    """
    Fetch all courses with their enrolled students.
    """
    try:
        response = requests.get(f"{COURSE_SERVICE}/with-students")
        response.raise_for_status()
        courses = response.json()
        return f"Courses with students: {courses}"
    except requests.RequestException as e:
        return f"Error fetching courses with students: {str(e)}"

@tool
def get_courses_with_professors() -> str:
    """
    Fetch all courses with their professors.
    """
    try:
        response = requests.get(f"{COURSE_SERVICE}/with-professors")
        response.raise_for_status()
        courses = response.json()
        return f"Courses with professors: {courses}"
    except requests.RequestException as e:
        return f"Error fetching courses with professors: {str(e)}"

@tool
def create_course(name: str, professor_id: int = None) -> str:
    """
    Create a new course with a name and optional professor ID.
    """
    try:
        payload = {"id": None, "name": name}
        if professor_id is not None:
            payload["professor"] = {"id": professor_id}
        response = requests.post(f"{COURSE_SERVICE}/create", json=payload)
        response.raise_for_status()
        course = response.json()
        return f"Course created: {course.get('name')} (ID: {course.get('id')})"
    except requests.RequestException as e:
        return f"Error creating course: {str(e)}"
    


course_tools=[get_courses_by_student_id, get_all_courses_with_students, get_courses_with_professors, create_course]