import matplotlib.pyplot as plt

#data
unemployment_rates = [3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0]
inflation_rates = [1.2, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]

#Create a scatter plot
plt.scatter(unemployment_rates, inflation_rates, color='blue', marker='o')

#Adding title and labels
plt.title('Relationship Between Inflation and Unemployment Rates', fontsize=14)
plt.xlabel('Unemployment Rate (%)', fontsize=12)
plt.ylabel('Inflation Rate (%)', fontsize=12)

plt.show()