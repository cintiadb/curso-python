import urllib.request
import json

def retrieve_all():
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    
    try:
        with urllib.request.urlopen(url) as response:
            data = json.load(response)
        active_courses = []

        for course in data:
            if course.get('enabled', False):
                full_name = course.get('fullName', '')
                name = course.get('name', '')
                year = int(course.get('year', 0))
                exercises_sum = sum(course.get('exercises', []))
                active_courses.append((full_name, name, year, exercises_sum))
        
        return active_courses
    
    except Exception as e:
        print(f"Error: {e}")
        return []

courses = retrieve_all()
print(courses)