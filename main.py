import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =========================== #
#   LOAD THE DATASET
# =========================== #
# Your CSV must have columns like:
# Name, Marks
df = pd.read_csv("marks.csv")

# =========================== #
#   BASIC STATISTICS
# =========================== #
marks = df["Marks"]

mean_val = np.mean(marks)
median_val = np.median(marks)
mode_val = marks.mode()[0]

print("Mean:", mean_val)
print("Median:", median_val)
print("Mode:", mode_val)

# =========================== #
#   MIN & MAX MARKS
# =========================== #
highest = marks.max()
lowest = marks.min()

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

# =========================== #
#   PASS / FAIL COUNT
# =========================== #
pass_mark = 33
passed = (marks >= pass_mark).sum()
failed = (marks < pass_mark).sum()

print("Passed:", passed)
print("Failed:", failed)

# =========================== #
#   TOP 5 STUDENTS
# =========================== #
top_5 = df.sort_values(by="Marks", ascending=False).head(5)
print("\nTop 5 Students:")
print(top_5)

# =========================== #
#   GRADE DISTRIBUTION
# =========================== #
def grade(m):
    if m >= 90: return "A"
    elif m >= 75: return "B"
    elif m >= 60: return "C"
    elif m >= 40: return "D"
    else: return "F"

df["Grade"] = df["Marks"].apply(grade)

print("\nGrade Distribution:")
print(df["Grade"].value_counts())

# =========================== #
#   HISTOGRAM OF MARKS
# =========================== #
plt.figure(figsize=(8,5))
plt.hist(marks, bins=10)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# =========================== #
#   BAR CHART OF GRADES
# =========================== #
grade_counts = df["Grade"].value_counts()

plt.figure(figsize=(8,5))
grade_counts.plot(kind="bar")
plt.title("Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Number of Students")
plt.show()
