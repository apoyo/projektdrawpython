import matplotlib.pyplot as plt

# defining labels
activities = ['eat', 'sleep', 'work', 'play']

# portion covered by each label
slices = [3, 7, 8, 6]

# color for each label
colors = ['#000000', '#FFFFFF', '#999999']

# plotting the pie chart
plt.pie(slices, labels = activities, colors=colors, 
        

# plotting legend
plt.legend()

# showing the plot
plt.show()