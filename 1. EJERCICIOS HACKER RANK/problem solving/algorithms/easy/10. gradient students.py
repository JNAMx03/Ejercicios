def gradingStudents(grades):
    for i in range(len(grades)):
        
        for j in range(5):
            x = grades[i]+j
            if x % 5 == 0:
                y = x - grades[i]
                if y < 3 and x >= 40:
                    grades[i] = x
                
    return grades
            
                

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()