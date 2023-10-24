class Student:

    def __init__(self):
        self.scores = []

    def input_scores(self):
        self.scores = list(map(int,input().split()))

    def calculate_total_scores(self):
        return sum(self.scores)
    

n = int(input("Enter the total number of students:"))

kristen = Student()

kristen.input_scores()

count_higer = 0

for i in range(n-1):
    student = Student()

    student.input_scores()

    total_score_others = student.calculate_total_scores()

    if( total_score_others > kristen.calculate_total_scores()):
        count_higer += 1


print(count_higer)