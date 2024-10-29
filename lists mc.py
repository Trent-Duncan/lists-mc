# Trent Duncan
# 10/29/24
# Lists mc

# Start with an empty list
first_names = []
last_names = []
schools = []
courses = []
student1_scores = []
student2_scores = []


# Use append ( ) method to add data to the list
first_names.append('Trent')
first_names.append('Joey')

last_names.append('Duncan')
last_names.append('Robertson')

schools.append('West Senior High')
schools.append('Algebra')

courses.append('Chemistry')
courses.append('Algebra')

student1_scores.append(88)
student1_scores.append(75)
student1_scores.append(92)
student1_scores.append(80)


student2_scores.append(75)
student2_scores.append(70)
student2_scores.append(100)
student2_scores.append(80)


# Print the list of first names
# print(first_names)
# print(last_names)

# print(f'The first student is: {first_names[0]} {last_names[0]}')
# print(f'The second student is: {first_names[1]} {last_names[1]}')

print(student1_scores)

average_test_score1 = sum(student1_scores) / len(student1_scores)
print(f'Average test score for Student 1: {average_test_score1}')

average_test_score2 = sum(student2_scores) / len(student2_scores)
print(f'Average test score for Student 2: {average_test_score2}')
