# 20201213 - Get Student Names
def get_student_names(students):
    ans = []
    for v in students.values():
        ans.append(v)
    ans.sort()
    return ans


get_student_names({
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
})