import marks
import report

with open("D:\PythonPractice\mini_projects\project4\students.txt", "r") as file:

    for line in file:
        if line.strip() == "":
            continue

        data = line.strip().split(",")

        name = data[0]
        marks_list = list(map(int, data[1:]))

        total = marks.calculate_total(marks_list)
        avg = marks.calculate_average(marks_list)

        report.print_report(name, total, avg)
        print("-" * 30)


# note -- where ur file store here add path correctly other wise it gives error
# with open(r"D:\PythonPractice\mini_projects\project4\students.txt", "r") as file: like this
