import numpy as np
import matplotlib.pyplot as plt

# Sales figures for different product categories
X = ['Electronics', 'Clothing', 'Food', 'Books']
Y_Q1_Sales = [10000, 8000, 12000, 5000]  # Sales in Q1
Y_Q2_Sales = [12000, 9000, 15000, 6000]  # Sales in Q2
Y_Q3_Sales = [15000, 10000, 18000, 7000]  # Sales in Q3
Y_Q4_Sales = [20000, 12000, 22000, 8000]  # Sales in Q4

# Create positions for each bar (adjusted for clarity)
bar_width = 0.2  # Adjust bar width as needed
index = np.arange(len(X))
Q1_pos = index - 1.5 * bar_width
Q2_pos = index - 0.5 * bar_width
Q3_pos = index + 0.5 * bar_width
Q4_pos = index + 1.5 * bar_width

# Create the bar chart
plt.bar(Q1_pos, Y_Q1_Sales, bar_width, label='Q1 Sales')
plt.bar(Q2_pos, Y_Q2_Sales, bar_width, label='Q2 Sales')
plt.bar(Q3_pos, Y_Q3_Sales, bar_width, label='Q3 Sales')
plt.bar(Q4_pos, Y_Q4_Sales, bar_width, label='Q4 Sales')

# Set x-axis labels and title
plt.xticks(index, X, rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.xlabel("Product Category")
plt.ylabel("Sales (in thousands)")
plt.title("Sales Comparison by Quarter")

# Add a legend
plt.legend()

# Display the chart
plt.tight_layout()  # Adjust spacing for better visualization
plt.show()