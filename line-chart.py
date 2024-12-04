import matplotlib.pyplot as plt
import numpy as np

#Data
days = np.arange(0, 10, 1)
disease_progression = [10, 9, 7, 6, 5, 4, 3, 2, 2, 1]
treatment_outcomes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Create the line chart
plt.plot(days, disease_progression, label='Disease Progression', marker='o', color='red')
plt.plot(days, treatment_outcomes, label='Treatment Outcomes', marker='o', color='blue')

#Adding titles and labels
plt.title('Disease Progression and Treatment Outcomes Over Time')
plt.xlabel('Days of Treatment')
plt.ylabel('Score')
plt.legend()


plt.show()