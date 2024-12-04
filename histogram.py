import matplotlib.pyplot as plt

#Customer spending amounts in dollars
customer_spending = [25, 47, 53, 23, 67, 89, 120, 45, 30, 80, 95, 60, 55, 40, 75, 90, 65, 85, 50, 100]

# Create a histogram
plt.hist(customer_spending, bins=10, color='blue', edgecolor='black')
#bins means the intervals or categories into which the data is divided. In this case, it is 10.

# Add a title and labels
plt.title('Customer Spending Distribution')
plt.xlabel('Spending Amount ($)')
plt.ylabel('Frequency')

# Show the chart
plt.show()