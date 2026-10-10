students = [
    {"name": "Alice", "grades": [5, 4, 5, 3]},
    {"name": "Bob", "grades": [4, 4, 4, 5]},
    {"name": "Charlie", "grades": [5, 5, 5, 5]},
]

average_grades=[{i['name']: sum(i["grades"])/len(i["grades"]) } for i in students]
max_grade=max(average_grades, key=lambda d:list(d.values())[0])

print(average_grades)

print(max_grade)



