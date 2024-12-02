import matplotlib.pyplot as plt

# [Name, ID, Attendance (%), Grade (%)]
students = [
    ['John Doe', 101, 85.5, 92.0],
    ['Jane Smith', 102, 78.0, 88.5],
    ['Alice Johnson', 103, 93.0, 95.0],
    ['Bob Brown', 104, 65.0, 70.0],
    ['Emily Davis', 105, 80.0, 82.5],
    ['Michael Wilson', 106, 72.5, 75.0],
    ['Sarah Lee', 107, 89.0, 91.5],
    ['David Green', 108, 95.0, 97.0],
    ['Laura White', 109, 70.5, 60.0],
    ['James Clark', 110, 88.0, 85.0]
]

attendance = [student[2] for student in students]
grades = [student[3] for student in students]

# Doe de voorspellingen met een verzonnen formule
voorspellingen = [24 + 0.7 * x for x in attendance]

plt.scatter(attendance, grades, color="purple")
plt.plot(attendance, voorspellingen, color="orange")

plt.title("titel")
plt.xlabel("Attendance (%)")
plt.ylabel("Grade (0-100)")

plt.savefig("scatterplot.png")
plt.show()