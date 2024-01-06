# Create portfolio returns for the two sub-periods using the list of asset returns
asset_returns
portfolio_returns = np.array([ x.dot(weights) for x in asset_returns])

# Derive portfolio losses from portfolio returns
losses = - portfolio_returns

# Find the historical simulated VaR estimates
VaR_95 = [np.quantile(x, 0.95) for x in losses]

# Display the VaR estimates
print("VaR_95, 2005-2006: ", VaR_95[0], '; VaR_95, 2007-2009: ', VaR_95[1])


# Created mean asset losses in Numpy array mu
mu

# Create efficient covariance matrix, we're using the daily, not annualized variance as in previous exercises
e_cov

total_steps = 1440
N = 10000

# Initialize daily cumulative loss for the 4 assets, across N runs
daily_loss = np.zeros((4 , N))

# Create the Monte Carlo simulations for N runs
for n in range(N):
    # Compute simulated path of length total_steps for correlated returns
    correlated_randomness = e_cov @ norm.rvs(size = (4,total_steps))
    # Adjust simulated path by total_steps and mean of portfolio losses
    steps = 1/total_steps
    minute_losses = mu * steps + correlated_randomness * np.sqrt(steps)
    daily_loss[:, n] = minute_losses.sum(axis=1)
    
# Generate the 95% VaR estimate
losses = weights @ daily_loss
print("Monte Carlo VaR_95 estimate: ", np.quantile(losses, 0.95))
