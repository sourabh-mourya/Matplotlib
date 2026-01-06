import matplotlib.pyplot as plt

"""
SUBPLOT – CONCEPT NOTES

Subplot ka matlab hota hai:
Ek hi figure (window/page) ke andar
multiple graphs ko show karna.

Example:
- Line chart -> Sales show karta hai
- Bar chart  -> Expenses show karta hai

Agar hum in graphs ko alag-alag draw karein,
to har graph alag window mein open hoga.

Lekin jab hume:
- comparison karna ho
- ek saath multiple charts dekhne ho

tab hum subplot ka use karte hain.
"""

# ---------------------------------------------------
# USE CASES OF SUBPLOT
# ---------------------------------------------------

"""
Subplot ke use cases:

- Jab multiple charts ke saath kaam karna ho
- Jab do ya zyada graphs ke beech data compare karna ho
- Exploratory Data Analysis (EDA)
- Machine Learning algorithms ke visualization
- Business dashboards
"""

# ---------------------------------------------------
# SUBPLOT CREATE KARNE KE 2 TARIKE
# ---------------------------------------------------

"""
1) pyplot (Functional) approach
2) Object Oriented (OO) approach
"""

# ---------------------------------------------------
# 1) FIRST WAY – plt.subplot() FUNCTION
# ---------------------------------------------------

"""
plt.subplot() directly grid create karta hai.

Syntax:
plt.subplot(nrows, ncols, index)

- nrows  -> number of rows
- ncols  -> number of columns
- index  -> position (1-based indexing)
"""

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 35, 23]
#
# # First subplot (1 row, 2 columns, 1st position)
# plt.subplot(1, 2, 1)
# plt.plot(x, y)
# plt.title('Line Chart (Sales)')
#
# # Second subplot (1 row, 2 columns, 2nd position)
# plt.subplot(1, 2, 2)
# plt.bar(x, y)
# plt.title('Bar Chart (Expenses)')
#
# plt.show()

"""
Note:
plt.subplot() small examples ke liye theek hai,
lekin large projects mein manage karna thoda difficult hota hai.
"""

# ---------------------------------------------------
# 2) SECOND WAY – OBJECT ORIENTED APPROACH
# ---------------------------------------------------

"""
Object Oriented approach real-world projects mein use hota hai.

Syntax:
fig, ax = plt.subplots(nrows, ncols, figsize=(width, height))

- fig      -> overall figure (window)
- ax       -> individual subplot objects
- figsize -> optional (figure ka size)
"""

# fig, ax = plt.subplots(1, 2, figsize=(10, 5))
# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 35, 23]
#
# ax[0].plot(x, y)
# ax[0].set_title('Line Plot')
#
# ax[1].bar(x, y)
# ax[1].set_title('Bar Chart')
#
# plt.tight_layout()
# plt.show()

"""
Why Object Oriented approach is better?
- Code readable hota hai
- Large datasets ke saath easy handling
- Individual subplot ko easily customize kar sakte hain
"""

# ---------------------------------------------------
# INDIVIDUAL SUBPLOTS CUSTOMIZATION
# ---------------------------------------------------

"""
Har subplot ko alag-alag customize kiya ja sakta hai:
- color
- title
- labels
- grid
"""

fig, ax = plt.subplots(1, 2, figsize=(10, 5))

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 35, 23]

# Line Chart
ax[0].plot(x, y, color='green')
ax[0].set_title('Line Plot (Sales)')
ax[0].set_xlabel('Days')
ax[0].set_ylabel('Sales')

# Bar Chart
ax[1].bar(x, y, color='pink')
ax[1].set_title('Bar Chart (Expenses)')
ax[1].set_xlabel('Days')
ax[1].set_ylabel('Expenses')

# Overall title for entire figure
fig.suptitle('Comparison of Line and Bar Charts')

"""
plt.tight_layout():
Automatically spacing adjust karta hai
taaki titles aur labels overlap na karein.

Note:
tight_layout() hamesha plt.show() se pehle use hota hai.
"""

plt.tight_layout()
plt.show()



"""
SUBPLOT – ADVANCED NOTES (ADDED CONTENT)

Subplot sirf graphs ko ek page par laane ke liye hi nahi,
balki unke beech comparison, analysis aur debugging ke liye bhi use hota hai.

IMPORTANT INTERVIEW / VIVA POINT:
"Subplot helps in visual comparison of multiple datasets 
within the same coordinate system."
"""

# ---------------------------------------------------
# EXTRA IMPORTANT CONCEPTS (ADDED)
# ---------------------------------------------------

"""
1) sharex & sharey:
Agar multiple subplots ka X-axis ya Y-axis same ho,
to hum unhe share karwa sakte hain.

Isse:
- comparison easy hota hai
- axis values repeat nahi hoti
"""

# ---------------------------------------------------
# SHAREX / SHAREY EXAMPLE
# ---------------------------------------------------

fig, ax = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

days = [1, 2, 3, 4, 5]
sales = [100, 200, 150, 300, 250]
expenses = [80, 120, 100, 200, 180]

ax[0].plot(days, sales, color='blue')
ax[0].set_title('Daily Sales')
ax[0].set_ylabel('Sales')

ax[1].plot(days, expenses, color='red')
ax[1].set_title('Daily Expenses')
ax[1].set_ylabel('Expenses')
ax[1].set_xlabel('Days')

plt.tight_layout()
plt.show()

"""
INTERVIEW TIP:
sharex=True ka matlab:
neeche wale subplot ka X-axis dono ke liye common hoga
"""

# ---------------------------------------------------
# 2x2 GRID SUBPLOT (VERY IMPORTANT)
# ---------------------------------------------------

"""
2x2 subplot ka use tab hota hai jab:
- 4 different metrics ko compare karna ho
- dashboard-style visualization banana ho
"""

fig, ax = plt.subplots(2, 2, figsize=(10, 8))

ax[0, 0].plot(days, sales, color='green')
ax[0, 0].set_title('Sales Line Chart')

ax[0, 1].bar(days, sales, color='orange')
ax[0, 1].set_title('Sales Bar Chart')

ax[1, 0].plot(days, expenses, color='purple')
ax[1, 0].set_title('Expenses Line Chart')

ax[1, 1].bar(days, expenses, color='pink')
ax[1, 1].set_title('Expenses Bar Chart')

fig.suptitle('Sales vs Expenses Dashboard')
plt.tight_layout()
plt.show()

"""
VIVA QUESTION:
Q: ax[1,1] ka matlab kya hai?
A: 2nd row aur 2nd column ka subplot
"""

# ---------------------------------------------------
# COMMON MISTAKES (EXAM POINT)
# ---------------------------------------------------

"""
Common mistakes students make:

1) plt.show() se pehle tight_layout() na lagana
2) ax aur plt ko mix kar dena (OO approach mein)
3) subplot indexing 0-based aur 1-based ko confuse karna
4) Too many subplots in small figsize
"""

# ---------------------------------------------------
# REAL WORLD + ML USE CASE (ADDED)
# ---------------------------------------------------

"""
Machine Learning Example:
- Subplot 1: Training Loss
- Subplot 2: Validation Loss

Agar dono curves paas-paas ho:
-> Model achha perform kar raha hai
Agar gap zyada ho:
-> Overfitting
"""

epochs = [1, 2, 3, 4, 5]
train_loss = [0.9, 0.6, 0.4, 0.3, 0.2]
val_loss = [1.0, 0.8, 0.6, 0.5, 0.45]

fig, ax = plt.subplots(1, 2, figsize=(10, 4))

ax[0].plot(epochs, train_loss, label='Training Loss')
ax[0].set_title('Training Loss')
ax[0].legend()

ax[1].plot(epochs, val_loss, label='Validation Loss', color='red')
ax[1].set_title('Validation Loss')
ax[1].legend()

fig.suptitle('Model Performance Analysis')
plt.tight_layout()
plt.show()

"""
FINAL LINE (EXAM READY):
Subplot is a powerful visualization technique used to analyze,
compare, and debug multiple datasets efficiently on a single figure.
"""
