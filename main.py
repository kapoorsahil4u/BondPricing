import numpy as np
import numpy_financial as npf
import pandas as pd
import matplotlib.pyplot as plt

# Create an array of bond yields and convert to DataFrame
bond_yields = np.arange(0, 20, 0.1)
bond = pd.DataFrame(bond_yields, columns=['bond_yield'])

# Add columns for different bonds
bond['bond_price_5Y'] = -npf.pv(rate=bond['bond_yield'] / 100, nper=5, pmt=5, fv=100)
bond['bond_price_10Y'] = -npf.pv(rate=bond['bond_yield'] / 100, nper=10, pmt=5, fv=100)

# Plot graph of bonds
plt.plot(bond['bond_yield'], bond['bond_price_5Y'], label='5 Year Bond')
plt.plot(bond['bond_yield'], bond['bond_price_10Y'], label='10 Year Bond')
plt.xlabel('Yield (%)')
plt.ylabel('Bond Price (USD)')
plt.legend()
plt.show()

print('-----------------Validate the bond trading price at premium or at discount and \n a comparetive study of coupon rate and yield rate')
# Bond with price of USD 92 paying 3% coupon for 3 years
bond_a = npf.rate(nper=3, pmt=3, pv=-92, fv=100)
print("Bond A: ", bond_a)  # Since PV =92 Which is undervalued (or Discounted) hence its Yield is to be greater than Coupon rate

# Bond with price of USD 102 paying 6% coupon for 5 years
bond_b = npf.rate(nper=5, pmt=6, pv=-102, fv=100)
print("Bond B: ", bond_b)

# Bond with price of USD 95 paying 3% coupon for 5 years
bond_c = npf.rate(nper=5, pmt=3, pv=-95, fv=100)
print("Bond C: ", bond_c)


print('-----Understand the concept of Duration - Interest rate sensitivity of two bonds')
# Price a 10 year bond with 3% annual coupon at 3% yield and print
bond_1 = -npf.pv(rate=0.03, nper=10, pmt=3, fv=100)
print("10 Year Bond 3% Yield: ", bond_1)

# Price a 10 year bond with 3% annual coupon at 4% yield and print
bond_2 = -npf.pv(rate=0.04, nper=10, pmt=3, fv=100)
print("10 Year Bond 4% Yield: ", bond_2)

# Price a 20 year bond with 3% annual coupon at 3% yield and print
bond_3 = -npf.pv(rate=0.03, nper=20, pmt=3, fv=100)
print("20 Year Bond 3% Yield: ", bond_3)

# Price a 20 year bond with 3% annual coupon at 4% yield and print
bond_4 = -npf.pv(rate=0.04, nper=20, pmt=3, fv=100)
print("20 Year Bond 4% Yield: ", bond_4)

print('--------Check for Duration of a Zero coupon and coupon bond duration')
# Find the price of the zero coupon bond at current yield levels
price = -npf.pv(rate=0.03, nper=10, pmt=0, fv=100)

# Find the price of the zero coupon bond at 1% higher yield levels
price_up = -npf.pv(rate=0.04, nper=10, pmt=0, fv=100)

# Find the price of the zero coupon bond at 1% lower yield levels
price_down = -npf.pv(rate=0.02, nper=10, pmt=0, fv=100)

# Calculate duration using the formula and print result
duration = (price_down - price_up) / (2 * price * 0.01)
print("Zero Coupon Bond Duration: ", duration)

print('--------Check for Duration of a coupon paying')
# Find the price of the coupon bond at current yield levels (yield = 3%)
price = -npf.pv(rate=0.03, nper=10, pmt=3, fv=100)

# Find the price of the coupon bond at 1% higher yield levels
price_up = -npf.pv(rate=0.04, nper=10, pmt=3, fv=100)

# Find the price of the coupon bond at 1% lower yield levels
price_down = -npf.pv(rate=0.02, nper=10, pmt=3, fv=100)

# Calculate duration using the formula
duration = (price_down - price_up) / (2 * price * 0.01)

# Print the result
print("Coupon Paying Bond Duration: ", duration)


print('--------Comparing the duration of two bonds directly: 10 year bond with 3% coupon & 5% yield,20 year bond with 3% coupon & 5% yield  ')
# Find & print duration of 10 year bond with 3% coupon & 5% yield
price_10y = -npf.pv(rate=0.05, nper=10, pmt=3, fv=100)
price_up_10y = -npf.pv(rate=0.06, nper=10, pmt=3, fv=100)
price_down_10y = -npf.pv(rate=0.04, nper=10, pmt=3, fv=100)
duration_10y = (price_down_10y - price_up_10y) / (2 * price_10y * 0.01)
print("10 Year Bond: ", duration_10y)

# Find & print duration of 20 year bond with 3% coupon & 5% yield
price_20y = -npf.pv(rate=0.05, nper=20, pmt=3, fv=100)
price_up_20y = -npf.pv(rate=0.06, nper=20, pmt=3, fv=100)
price_down_20y = -npf.pv(rate=0.04, nper=20, pmt=3, fv=100)
duration_20y = (price_down_20y - price_up_20y) / (2 * price_20y * 0.01)
print("20 Year Bond: ", duration_20y)

print('--------Using the steepness of the price/yield line')
# Create an array of bond yields
bond_yields = np.arange(0, 20, 0.1)

# Convert this array into a pandas DataFrame and add column title
bond = pd.DataFrame(bond_yields, columns=['bond_yield'])

# Add bond price column with price varying according to the yield
bond['bond_price'] = -npf.pv(rate=bond['bond_yield'] / 100, nper=20, pmt=5, fv=100)

# Plot graph of bond yields against prices, add x-axis and y-axis labels, show plot
plt.plot(bond['bond_yield'], bond['bond_price'])
plt.xlabel('Yield (%)')
plt.ylabel('Bond Price (USD)')
plt.show()

print('--------Plotting duration vs. the factor')
# Create array of coupon rates and assign to pandas DataFrame
bond_coupon = np.arange(0, 10, 0.1)
bond = pd.DataFrame(bond_coupon, columns=['bond_coupon'])

# Calculate bond price, price_up, price_down, and duration
bond['price'] = -npf.pv(rate=0.05, nper=10, pmt=bond['bond_coupon'], fv=100)
bond['price_up'] = -npf.pv(rate=0.05 + 0.01, nper=10, pmt=bond['bond_coupon'], fv=100)
bond['price_down'] = -npf.pv(rate=0.05 - 0.01, nper=10, pmt=bond['bond_coupon'], fv=100)
bond['duration'] = (bond['price_down'] - bond['price_up']) / (2 * bond['price'] * 0.01)

# Plot coupon vs. duration, add labels & title, show plot
plt.plot(bond['bond_coupon'], bond['duration'])
plt.xlabel('Coupon (%)')
plt.ylabel('Duration (%)')
plt.show()
