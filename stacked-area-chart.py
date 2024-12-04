import matplotlib.pyplot as plt
import numpy as np

#data
years = np.array([2000, 2005, 2010, 2015, 2020])
population_a = np.array([300, 500, 550, 700, 990])  
population_b = np.array([250, 400, 600, 750, 950]) 

#Creating the stacked area chart
plt.stackplot(years, population_a, population_b, labels=['Country A', 'Country B'], colors=['blue', 'red'])

#Adding labels and title
plt.title('Population Growth - Stacked Area Chart')
plt.xlabel('Year')
plt.ylabel('Population (in billions)')
plt.legend(loc='upper left')

#To ensure x-axis (years) is displayed as whole numbers with decimal points
plt.xticks(years)
plt.show()