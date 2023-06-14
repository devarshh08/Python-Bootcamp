student_scores = {
  "Harry":91,
  "Ron":100,
  "Hermoine":69,
  "Draco":71,
  "Wolverine":80,
  "Neville":81,
  "Marvin":90,
  "Kevin":70
}

student_grades = {}

for key in student_scores:
  if (student_scores[key])>90 and (student_scores[key])<=100:
    student_grades[key] = "Outstanding"
  elif (student_scores[key])>80 and (student_scores[key])<=90:
    student_grades[key] = "Exceeds Expectation"
  elif (student_scores[key])>70 and (student_scores[key])<=80:
    student_grades[key] = "Acceptable"
  else:
    student_grades[key] = "Fail"

print(student_grades)