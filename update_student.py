import json

with open("student.json", "r") as file:
    json_string = file.read()

student_data = json.loads(json_string)

student_data["name"] = "Visar"

with open("student.json", "w") as file:
    json.dump(student_data, file, indent=4)

print("Student name updated successfully!")

