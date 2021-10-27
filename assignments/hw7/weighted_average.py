"""
Name: Jeremy Miller
weighted_average.py

Problem: This program calculates the weighted averages of students' grades

Certificate of Authenticity:
I certify that this assignment is entirely my own work
"""


def main():
    weighted_average('grades.txt', 'avg.txt')


def weighted_average(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    count = 0
    class_total = 0
    for line in in_file:
        split_line = line.split(": ")
        values = split_line[1].split()
        grades = 0
        weight_total = 0
        for num in range(0, len(values)-1, 2):
            weight = values[num]
            grade = values[num+1]
            weight_total = weight_total + float(weight)
            grades = grades + (float(grade) * float(weight))
        if weight_total == 100:
            avg = grades / 100
            class_total = class_total + avg
            print(split_line[0] + "'s average:", round(avg, 1), file=out_file)
        elif weight_total < 100:
            count = count + 1
            print(split_line[0] + "'s average: Error: The weights are less than 100.", file=out_file)
        else:
            count = count + 1
            print(split_line[0] + "'s average: Error: The weights are more than 100.", file=out_file)

    in_file2 = open(in_file_name, 'r')
    contents = in_file2.readlines()
    class_avg = class_total / (len(contents) - count)
    print("Class average:", round(class_avg, 1), file=out_file)
    in_file.close()
    out_file.close()
    in_file2.close()


if __name__ == '__main__':
    main()
