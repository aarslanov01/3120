# Run a Monte Carlo simulation 500 times using a mean_inflation of 2 and a mean_volume of 500
cov_matrix

def profit_next_year_mc(mean_inflation, mean_volume, n):
  profits = []
  for i in range(n):
    # Generate inputs by sampling from the multivariate normal distribution
    rate_sales_volume = st.multivariate_normal.rvs(mean=[mean_inflation,mean_volume], cov=cov_matrix,size=1000)
    # Deterministic calculation of company profit
    price = 100 * (100 + rate_sales_volume[:,0])/100
    volume = rate_sales_volume[:,1]
    loan_and_cost = 50 * volume + 45 * (100 + 3 * rate_sales_volume[:,0]) * (volume/100)
    profit = (np.mean(price * volume - loan_and_cost))
    profits.append(profit)
  return profits

profits = profit_next_year_mc(2,500,500)

# Create a displot of the results
sns.displot(profits)
plt.show()

# Company sensitivity analysis
x1 = []
x2 = []
y = []
# The mean inflation percentages are 0, 1, 2, 5, 10, 15, 20, 50, 
# while the sales values for use as the mean volume value are 100, 200, 500, 800, 1000
for infl in [0, 1, 2, 5, 10, 15, 20, 50]:
    for vol in [100, 200, 500, 800, 1000]:
		# Run profit_next_year_mc so that it samples 100 times for each infl and vol combination
        avg_prof = np.mean(profit_next_year_mc(infl,vol,100))
        x1.append(infl)
        x2.append(vol)
        y.append(avg_prof)
df_sa = pd.concat([pd.Series(x1), pd.Series(x2), pd.Series(y)], axis=1)
df_sa.columns = ["Inflation", "Volume", "Profit"]
# Create a displot of the simulation results for "Profit"
sns.displot(df_sa['Profit'])
plt.show()

# Visualize sensitivity analysis results
df_sa.plot.hexbin(x='Inflation',
     y='Volume',
     C='Profit',
     reduce_C_function=np.mean,
     gridsize=10,
     cmap="viridis",
     sharex=False)
plt.show()
