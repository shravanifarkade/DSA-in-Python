# Problem Statement: Imagine you are developing a system to manage student grades in a school. The
# grades are stored in a matrix where rows represent students, and columns represent subjects. However,
# most students do not take all subjects, resulting in a sparse matrix where most elements are zero.
# Given the sparse matrix representing student grades below, implement a solution using arrays to
# efficiently manage and manipulate the grades data:

# Perform operations such as calculating the average grade for each subject, identifying students with the
# highest grades, and finding the subject with the highest average grade.
class StudentGrades:
    def __init__(self, grades):
        self.grades = grades  # 2D list representing the sparse matrix

    def average_per_subject(self):
        subject_averages = []
        for j in range(len(self.grades[0])):  # Iterate through each subject
            total = 0
            count = 0
            for i in range(len(self.grades)):  # Iterate through each student
                if self.grades[i][j] != 0:  # Only consider non-zero grades
                    total += self.grades[i][j]
                    count += 1
            if count > 0:
                subject_averages.append(total / count)
            else:
                subject_averages.append(0)  # No grades for this subject
        return subject_averages

    def highest_grades_per_student(self):
        highest_grades = {}
        for i in range(len(self.grades)):
            highest_grade = max(self.grades[i])  # Get the highest grade for the student
            highest_grades[f'Student {i+1}'] = highest_grade
        return highest_grades

    def subject_with_highest_average(self):
        subject_averages = self.average_per_subject()
        highest_avg = max(subject_averages)
        highest_subject_index = subject_averages.index(highest_avg)
        return highest_subject_index, highest_avg  # Return subject index and average

# Sample Sparse Matrix Representation (Rows: Students, Columns: Subjects)
# Example: 4 Students and 5 Subjects
grades = [
    [85, 0, 90, 0, 70],  # Student 1
    [0, 88, 0, 91, 0],   # Student 2
    [75, 0, 0, 0, 85],   # Student 3
    [0, 0, 80, 70, 0]    # Student 4
]

def main():
    student_grades = StudentGrades(grades)

    # Calculate average grades per subject
    averages = student_grades.average_per_subject()
    print("Average grades per subject:", averages)

    # Identify highest grades for each student
    highest_grades = student_grades.highest_grades_per_student()
    print("Highest grades per student:", highest_grades)

    # Find the subject with the highest average grade
    highest_subject_index, highest_avg = student_grades.subject_with_highest_average()
    print(f"Subject {highest_subject_index + 1} has the highest average grade: {highest_avg:.2f}")

if __name__ == "__main__":
    main()
