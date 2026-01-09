"==========================================================================="
"Intermediate Python: Chapter 1 - Matplotlib Scatter Plot Example"
"==========================================================================="
'''# Change the line plot below to a scatter plot
plt.plot(gdp_cap, life_exp)
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()


# Change the line plot below to a scatter plot
# plt.plot(gdp_cap, life_exp)
# plt.scatter(gdp_cap, life_exp)
# 
# # Put the x-axis on a logarithmic scale
# plt.xscale('log')
#   # # Show plot
# plt.show()


1.for visually representing the relationship between two continuous variables.
2.scatter plots are particularly useful when you have a large number of data points and want to see how they are distributed across the axes.
3.They help in identifying patterns, trends, and potential correlations between the variables.
4.In this example, we use a scatter plot to visualize the relationship between GDP per capita (gdp_cap) and life expectancy (life_exp).
5.By setting the x-axis to a logarithmic scale using plt.xscale('log'), we can better visualize data that spans several orders of magnitude, making it easier to observe trends and relationships in the data.



BUT FOR UNDERSTANDING THE DISTRIBUTION OF A SINGLE VARIABLE, A HISTOGRAM OR A BOX PLOT WOULD BE MORE APPROPRIATE.'''

"============================================================================"
"CUSTOMIZATION AND ENHANCEMENT TIPS"
"============================================================================"
'''
1. adding xaxis labels, y-axis labels, and a title to the scatter plot.
# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log') 

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel(xlab)
plt.ylabel(ylab)


# Add title
plt.title(title)


# After customizing, display the plot
plt.show()

2. adding custom tick marks to the x-axis of the scatter plot.

# Scatter plot
plt.scatter(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)

# After customizing, display the plot
plt.show()


3. using the population data to set the size of the markers in the scatter plot.

# Import numpy as np
import numpy as np

# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop*2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()

4. using the col list to set the color of the markers in the scatter plot, and setting the transparency of the markers using the alpha parameter.

# Specify c and alpha inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c=col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show()

5. adding text annotations to highlight specific countries on the scatter plot.

# Scatter plot
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')

# Add grid() call
plt.grid(True)

# Show the plot
plt.show()
'''

