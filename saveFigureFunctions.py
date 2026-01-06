import matplotlib.pyplot as plt

"""
WHY DO WE NEED TO SAVE A FIGURE?

Normally jab hum matplotlib ka graph banate hain,
toh woh sirf tab tak visible hota hai jab tak code run ho raha hota hai.

Agar:
- hume kisi presentation mein graph dikhana ho
- kisi report / assignment mein attach karna ho
- kisi client, teacher ya friend ko bhejna ho
- ya future ke liye record rakhna ho

toh sirf plt.show() kaafi nahi hota.

Is situation mein hum plt.savefig() ka use karte hain,
jisse graph ek image file ke form mein save ho jaata hai
(jaise PNG, JPG, PDF, SVG).
"""

# ---------------------------------------------------
# BASIC SAVEFIG SYNTAX
# ---------------------------------------------------

"""
plt.savefig(
    'filename.extension',
    dpi=value,
    bbox_inches='tight'
)

filename.extension  -> file ka naam + format (png, jpg, pdf)
dpi                 -> image quality / resolution
bbox_inches='tight'-> extra white space remove karta hai
"""

# ---------------------------------------------------
# EXAMPLE: SAVE A LINE PLOT
# ---------------------------------------------------

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

# Create plot
plt.plot(x, y, color='blue', marker='o')
plt.title('Simple Line Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')

# Save the figure
plt.savefig('line_plot.png', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()

"""
IMPORTANT POINTS (EXAM + PRACTICAL):

1) plt.savefig() hamesha plt.show() se PEHLE likhna chahiye
   warna kuch environments mein blank image save ho sakti hai.

2) dpi = 300 tab use karo jab:
   - report
   - research paper
   - printing
   - high quality output chahiye

3) dpi = 100 ya 150:
   - normal screen viewing ke liye sufficient hota hai

4) bbox_inches='tight':
   - unnecessary white margins remove karta hai
   - image ko clean aur professional banata hai
"""

# ---------------------------------------------------
# REAL WORLD USE CASES
# ---------------------------------------------------

"""
Data Science:
- Model performance graphs save karke reports mein use karte hain

Business / Marketing:
- Sales, revenue charts clients ko bhejne ke liye

Healthcare:
- Patient data trends ko documentation ke liye

Education:
- Assignments, notes, presentations ke liye

Machine Learning:
- Training vs Validation loss graphs ko track karne ke liye
"""

"""
FINAL ONE-LINER (INTERVIEW READY):

We save figures so that visualizations can be reused,
shared, printed, or documented without re-running the code.
"""
