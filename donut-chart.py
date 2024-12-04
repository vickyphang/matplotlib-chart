import matplotlib.pyplot as plt

#Data
labels = ['Fruits', 'Vegetables', 'Carbohydrates', 'Protein', 'Dairy']
sizes = [30, 25, 20, 15, 10]  # Percentage of each food type
colors = ['red','pink','yellow','green','blue']  # Colors for each segment

#Create the pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', wedgeprops=dict(width=0.5))  # Set width for the donut hole

#Equal aspect ratio ensures that pie chart is a circle
plt.axis('equal')  
plt.title('Composition of Different Types of Food in a Diet Plan')
    
plt.show()