from tools.student_tool import get_courses_by_student_id

# Direct test without LLM
if __name__ == "__main__":
    result = get_courses_by_student_id.invoke({"student_id": 1})
    print("Tool output:", result)
