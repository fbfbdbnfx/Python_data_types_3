students = [
    {"name": "Alice", "grades": [5, 4, 5, 3]},
    {"name": "Bob", "grades": [4, 4, 4, 5]},
    {"name": "Charlie", "grades": [5, 5, 5, 5]},
]

average_grades=[{i['name']: sum(i["grades"])/len(i["grades"]) } for i in students]

print(average_grades)

maxgrade=max(list(i.values()) for i in average_grades)
print(maxgrade)
