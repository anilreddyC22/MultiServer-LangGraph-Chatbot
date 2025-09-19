import requests
from langchain.tools import tool
from config.settings import PROFESSOR_SERVICE



@tool
def get_professors_with_multiple_courses() -> str:
    """
    Fetch professors who teach multiple courses.
    """
    try:
        response = requests.get(f"{PROFESSOR_SERVICE}/multiple-courses")
        response.raise_for_status()
        professors = response.json()
        if not professors:
            return "No professors found with multiple courses."
        names = [p['name'] if isinstance(p, dict) and 'name' in p else str(p) for p in professors]
        return f"Professors with multiple courses: {', '.join(names)}"
    except requests.RequestException as e:
        return f"Error fetching professors: {str(e)}"

@tool
def get_professor_for_course(course_id: int) -> str:
    """
    Fetch the professor for a given course ID.
    """
    try:
        response = requests.get(f"{PROFESSOR_SERVICE}/courses/{course_id}/professor")
        response.raise_for_status()
        professor = response.json()
        return f"Professor for course {course_id}: {professor.get('name', 'Unknown')}"
    except requests.RequestException as e:
        return f"Error fetching professor for course {course_id}: {str(e)}"

@tool
def get_students_by_professor(professor_id: int) -> str:
    """
    Fetch students taught by a specific professor.
    """
    try:
        response = requests.get(f"{PROFESSOR_SERVICE}/{professor_id}/students")
        response.raise_for_status()
        students = response.json()
        if not students:
            return f"No students found for professor {professor_id}."
        names = [s['name'] if isinstance(s, dict) and 'name' in s else str(s) for s in students]
        return f"Students taught by professor {professor_id}: {', '.join(names)}"
    except requests.RequestException as e:
        return f"Error fetching students for professor {professor_id}: {str(e)}"

@tool
def create_professor(name: str) -> str:
    """
    Create a new professor with the given name.
    """
    try:
        payload = {"id": None, "name": name}
        response = requests.post(f"{PROFESSOR_SERVICE}/create", json=payload)
        response.raise_for_status()
        professor = response.json()
        return f"Professor created: {professor.get('name')} (ID: {professor.get('id')})"
    except requests.RequestException as e:
        return f"Error creating professor: {str(e)}"
    


professor_tools = [get_professor_for_course, get_professors_with_multiple_courses, get_students_by_professor, create_professor]