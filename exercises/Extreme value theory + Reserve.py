'''
Examine the time series of block maxima for GE's losses over the period 2008 - 2009, 
using the .resample() method for three different block lengths: one week, one month, and one quarter, 
visualizing each series in a plot using the axis_* plot objects.
'''

# Resample the data into weekly blocks
weekly_maxima = losses.resample("W").max()
weekly_maxima
# Plot the resulting weekly maxima
axis_1.plot(weekly_maxima, label = "Weekly Maxima")
axis_1.legend()
plt.figure("weekly")
plt.show()

# Resample the data into monthly blocks
monthly_maxima = losses.resample("M").max()

# Plot the resulting monthly maxima
axis_2.plot(monthly_maxima, label = "Monthly Maxima")
axis_2.legend()
plt.figure("monthly")
plt.show()

# Resample the data into quarterly blocks
quarterly_maxima = losses.resample('Q').max()

# Plot the resulting quarterly maxima
axis_3.plot(quarterly_maxima, label = "Quarterly Maxima")
axis_3.legend()
plt.figure("quarterly")
plt.show()

# Plot the log daily losses of GE over the period 2007-2009
losses.plot()

# Find all daily losses greater than 10%
extreme_losses = losses[losses > 0.1]

# Scatter plot the extreme losses
extreme_losses.plot(style='o')
plt.show()

# Fit extreme distribution to weekly maximum of losses
fitted = genextreme.fit(weekly_max)

# Plot extreme distribution with weekly max losses historgram
x = np.linspace(min(weekly_max), max(weekly_max), 100)
plt.plot(x, genextreme.pdf(x, *fitted))
plt.hist(weekly_max, 50, density = True, alpha = 0.3)
plt.show()

# Compute the weekly block maxima for GE's stock
weekly_maxima = losses.resample("W").max()

# Fit the GEV distribution to the maxima
p = genextreme.fit(weekly_maxima)

# Compute the 99% VaR (needed for the CVaR computation)
VaR_99 = genextreme.ppf(0.95, *p)

# Compute the 99% CVaR estimate
CVaR_99 = (1 / (1 - 0.99)) * genextreme.expect(lambda x: x, 
           args=(p[0],), loc = p[1], scale = p[2], lb = VaR_99)

# Display the covering loss amount
print("Reserve amount: ", 1000000 * CVaR_99)
