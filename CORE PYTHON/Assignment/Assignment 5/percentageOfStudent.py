num_student = int(input('enter number of students:'))
total_per_sum = 0


for i in range(1, num_student+1):
    total_mark = 0
    print(f'enter marks for student {i}')

    total_marks = 0
    for j in range(1,6):
        marks = int(input(f'subject {j} marks:'))
        total_mark  = marks + total_mark
    
    print(f'Total_marks = {total_mark}')

    percentage = (total_mark / 500)*100
    total_per_sum = total_per_sum + percentage

    # print(f'Total_marks = {total_mark}')
    print(f'percentage of student {i} :{percentage}')

average_per = total_per_sum / num_student
print(f'Average percentage of student : {average_per}')