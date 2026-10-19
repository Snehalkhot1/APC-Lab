
import seaborn as sns
import matplotlib.pyplot as plt

students = ["Snehal", "Diya", "Priya", "Viraj", "Tanuja"]
marks = [78, 85, 92, 67, 88]

sns.barplot(x=students, y=marks)

plt.title("Student Marks in Python")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.ylim(0, 100)

plt.show()
