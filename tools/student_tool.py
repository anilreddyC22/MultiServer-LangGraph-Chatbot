import requests
from langchain.tools import tool
from config.settings import STUDENT_SERVICE


@tool
def get_courses_by_student_id(student_id: int) -> str:
    """
    Use this tool to fetch the list of courses that a student is enrolled in, 
    given the student's ID. 
    
    Example queries that should trigger this tool:
    - "Get courses for student 1"
    - "Which classes is student 2 taking?"
    - "List all courses for student ID 3"
    """
    try:
        #response = requests.get(f"{STUDENT_SERVICE}/{student_id}/courses")
        #response.raise_for_status()
        #courses = response.json()
        url = f"{STUDENT_SERVICE}/{student_id}/courses"
        print(f"[DEBUG] Requesting URL: {url}")   #  Log full URL
        response = requests.get(url)
        print(f"[DEBUG] Status: {response.status_code}")  #  Log status code
        print(f"[DEBUG] Response body: {response.text}")  #  Log raw response
        courses = response.json()

        if not courses:
            return f"No courses found for student with ID {student_id}."
        # Assuming each course is a dict with a 'name' field
        course_names = [c['name'] if isinstance(c, dict) and 'name' in c else str(c) for c in courses]
        return f"Courses enrolled by student {student_id}: {', '.join(course_names)}"
    except requests.RequestException as e:
        return f"Error fetching courses for student {student_id}: {str(e)}"

@tool
def get_students_by_course_ids(course_ids: str) -> str:
    """
    Fetch students enrolled in at least one of the given course IDs (comma-separated).
    """
    try:
        # course_ids should be a comma-separated string of IDs, e.g., "1,2,3"
        response = requests.get(f"{STUDENT_SERVICE}/by-courses", params={"ids": course_ids})
        response.raise_for_status()
        students = response.json()
        if not students:
            return f"No students found for course IDs: {course_ids}."
        # Assuming each student is a dict with a 'name' field
        student_names = [s['name'] if isinstance(s, dict) and 'name' in s else str(s) for s in students]
        return f"Students enrolled in courses {course_ids}: {', '.join(student_names)}"
    except requests.RequestException as e:
        return f"Error fetching students for course IDs {course_ids}: {str(e)}"
    
@tool
def get_students_with_common_courses():
    """
    Fetch students who share at least one course with the other students.
    """
    try:
        response = requests.get(f"{STUDENT_SERVICE}/common-courses")
        response.raise_for_status()
        students = response.json()
        if not students:
            return "No students found with common courses."
        student_names = [s['name'] if isinstance(s, dict) and 'name' in s else str(s) for s in students]
        return f"Students with common courses: {', '.join(student_names)}"
    except requests.RequestException as e:
        return f"Error fetching students with common courses: {str(e)}"
    
@tool
def get_course_from_common_courses_grouped():
    """
    Fetch courses that are common among groups of students.
    """
    try:
        response = requests.get(f"{STUDENT_SERVICE}/common-courses-grouped")
        response.raise_for_status()
        courses = response.json()
        if not courses:
            return "No common courses found among student groups."
        course_names = [c['name'] if isinstance(c, dict) and 'name' in c else str(c) for c in courses]
        return f"Common courses among student groups: {', '.join(course_names)}"
    except requests.RequestException as e:
        return f"Error fetching common courses among student groups: {str(e)}"
    
@tool
def get_students_shares_atleast_one_course(student_id: str):
    """
    Fetch students who share at least one course with the given student id.
    """
    try:
        response = requests.get(f"{STUDENT_SERVICE}/{student_id}/similar-students")
        response.raise_for_status()
        students = response.json()
        if not students:
            return "No students found who share at least one course."
        student_names = [s['name'] if isinstance(s, dict) and 'name' in s else str(s) for s in students]
        return f"Students who share at least one course: {', '.join(student_names)}"
    except requests.RequestException as e:
        return f"Error fetching students who share at least one course: {str(e)}"
    
@tool
def get_students_with_no_courses():
    """
    Fetch students who are not enrolled in any courses.
    """
    try:
        response = requests.get(f"{STUDENT_SERVICE}/students-with-no-courses")
        response.raise_for_status()
        students = response.json()
        if not students:
            return "All students are enrolled in at least one course."
        student_names = [s['name'] if isinstance(s, dict) and 'name' in s else str(s) for s in students]
        return f"Students with no courses: {', '.join(student_names)}"
    except requests.RequestException as e:
        return f"Error fetching students with no courses: {str(e)}"

@tool
def get_students_with_no_course_and_professor():
    """
    Fetch students who are not enrolled in any courses and have no assigned professor.
    """
    try:
        response = requests.get(f"{STUDENT_SERVICE}/students-with-no-course-and-professors")
        response.raise_for_status()
        students = response.json()
        if not students:
            return "All students are either enrolled in courses or have an assigned professor."
        student_names = [s['name'] if isinstance(s, dict) and 'name' in s else str(s) for s in students]
        return f"Students with no courses and no assigned professor: {', '.join(student_names)}"
    except requests.RequestException as e:
        return f"Error fetching students with no courses and no assigned professor: {str(e)}"
    
@tool
def get_students_by_courses(ids: str) -> str:
    """
    Fetch students enrolled in at least one of the given course IDs (comma-separated).
    Example: ids="1,2,3"
    """
    try:
        # Convert comma-separated string to set of integers for the request
        id_set = set(map(int, ids.split(',')))
        response = requests.get(f"{STUDENT_SERVICE}/by-courses", params={"ids": id_set})
        response.raise_for_status()
        students = response.json()
        if not students:
            return f"No students found for course IDs: {ids}."
        student_names = [s['name'] if isinstance(s, dict) and 'name' in s else str(s) for s in students]
        return f"Students enrolled in courses {ids}: {', '.join(student_names)}"
    except requests.RequestException as e:
        return f"Error fetching students for course IDs {ids}: {str(e)}"
    except Exception as e:
        return f"Invalid input or error: {str(e)}"

@tool
def get_students_in_all_courses(ids: str) -> str:
    """
    Fetch students who are enrolled in all available courses.
    """
    try:
        response = requests.get(f"{STUDENT_SERVICE}/by-all-courses", params={"ids": ids})
        response.raise_for_status()
        students = response.json()
        if not students:
            return "No students found who are enrolled in all courses."
        student_names = [s['name'] if isinstance(s, dict) and 'name' in s else str(s) for s in students]
        return f"Students enrolled in all courses: {', '.join(student_names)}"
    except requests.RequestException as e:
        return f"Error fetching students enrolled in all courses: {str(e)}"
    
@tool
def enroll_student_in_course(student_id: int, course_id: int) -> str:
    """
    Enroll a student in a course by student ID and course ID.
    """
    try:
        response = requests.post(f"{STUDENT_SERVICE}/{student_id}/enroll/{course_id}")
        response.raise_for_status()
        return response.text or "Student enrolled successfully."
    except requests.RequestException as e:
        return f"Error enrolling student {student_id} in course {course_id}: {str(e)}"
    
@tool
def create_student(name: str, course_ids: str = "") -> str:
    """
    Create a new student with a name and optional comma-separated course IDs.
    Example: create_student("John Doe", "1,2,3")
    """
    try:
        # Prepare courses as a list of dicts if course_ids are provided
        courses = []
        if course_ids:
            courses = [{"id": int(cid.strip())} for cid in course_ids.split(",") if cid.strip().isdigit()]
        payload = {
            "id": None,
            "name": name,
            "courses": courses
        }
        response = requests.post(f"{STUDENT_SERVICE}/create", json=payload)
        response.raise_for_status()
        student = response.json()
        return f"Student created: {student.get('name')} (ID: {student.get('id')})"
    except requests.RequestException as e:
        return f"Error creating student: {str(e)}"
    

    


student_tools = [
    get_courses_by_student_id,
    get_students_by_course_ids,
    get_students_with_common_courses,
    get_course_from_common_courses_grouped,
    get_students_shares_atleast_one_course,
    get_students_with_no_courses,
    get_students_with_no_course_and_professor,
    get_students_by_courses,
    get_students_in_all_courses,
    enroll_student_in_course,
    create_student,
]