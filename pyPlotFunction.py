import matplotlib.pyplot as plt

"""
plt.plot ka use line graph draw karne ke liye kiya jaata hai.
Jab hume do variables ke beech ka relationship dikhana hota hai,
tab hum line graph ka use karte hain.

plt.plot ke common parameters:
x-axis values
y-axis values
color      -> line ka color
linestyle  -> line ka pattern (solid, dashed, dotted)
linewidth  -> line ki thickness
marker     -> har data point ko highlight karta hai
label      -> legend ke liye line ka naam

Agar parameters pass na bhi karein to graph ban jaata hai,
lekin better visualization ke liye inka use karna chahiye.
"""

# ---------------- Line Graph Example ----------------
# months = [1, 2, 3, 4]
# sales = [1000, 1500, 1200, 1800]
#
# plt.plot(months, sales, color='red', linestyle='--', marker='o', label='2025 Sales Data')
# plt.xlabel('Months')
# plt.ylabel('Sales')
# plt.title('Monthly Sales Data Report')
# plt.legend(loc='upper left')
# plt.grid(color='gray', linestyle=':', linewidth=1)
# plt.xlim(1, 4)
# plt.ylim(0, 2000)
# plt.xticks([1, 2, 3, 4], ['M1', 'M2', 'M3', 'M4'])
# plt.show()


# ---------------------------------------------------
# Bar Chart, Pie Chart, Histogram – Concept Notes
# ---------------------------------------------------

"""
Bar Chart:
Category-wise comparison ke liye use hota hai
Example: Product sales comparison

Pie Chart:
Percentage distribution show karne ke liye use hota hai
5–6 categories tak best rehta hai

Histogram:
Data ka distribution aur spread dikhata hai
Example: Marks distribution
"""

# ---------------- Bar Chart Example ----------------
# products = ['A', 'B', 'C', 'D']
# sales = [1000, 1500, 800, 1200]
#
# plt.bar(products, sales, color='orange', label='Sales 2025')
# plt.xlabel('Products')
# plt.ylabel('Sales')
# plt.title('Product Sales Comparison')
# plt.legend()
# plt.show()


# ---------------- Pie Chart Example ----------------
"""
autopct='%1.1f%%' ka matlab:
Har slice ka percentage value show hogi
"""

# regions = ['North', 'South', 'East', 'West']
# revenue = [3000, 2000, 2500, 2300]
#
# plt.pie(
#     revenue,
#     labels=regions,
#     autopct='%1.1f%%',
#     colors=['gold', 'skyblue', 'lightgreen', 'coral']
# )
# plt.title('Regional Revenue Distribution')
# plt.show()


# ---------------- Histogram Example ----------------
# scores = [12, 32, 42, 21, 21, 34, 43, 56, 75, 13, 85, 37, 38, 35, 33]
#
# plt.hist(scores, bins=6, color='brown', edgecolor='black')
# plt.xlabel('Score Range')
# plt.ylabel('Number of Students')
# plt.title('Score Distribution of Students')
# plt.show()


# ---------------------------------------------------
# Scatter Plot
# ---------------------------------------------------

"""
Scatter plot ek data visualization technique hai
jisme data points (dots) ke form mein show hota hai.

Har point:
X-axis -> independent variable
Y-axis -> dependent variable

Use cases:
- Do variables ke beech correlation find karna
- Machine Learning (Regression)
- Outliers aur trend analysis
"""

# syntax:
# plt.scatter(x, y, color='color', marker='marker', label='label')

# ---------------- Scatter Plot (Two Groups) ----------------

# Group 1: Class A
plt.scatter([1, 2, 3], [50, 55, 60], color='blue', marker='o', label='Class A')

# Group 2: Class B
plt.scatter([1, 2, 3], [45, 50, 55], color='orange', marker='D', label='Class B')

plt.xlabel('Hours Studied')
plt.ylabel('Exam Score')
plt.title('Comparison Between Two Classes')
plt.legend()
plt.grid(True)
plt.show()
