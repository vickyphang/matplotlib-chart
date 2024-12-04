import matplotlib.pyplot as plt

# Data
players = ['Player A', 'Player B', 'Player C', 'Player D']
goals = [10, 15, 7, 12]

# Create a horizontal bar chart
plt.barh(players, goals, color='blue')

# Add a title and labels
plt.title('Goals Scored by Players')
plt.xlabel('Players')
plt.ylabel('Goals Scored')

# Show the chart
plt.show()