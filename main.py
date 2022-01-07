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


print('-------------------Dollar Duration and DV01(Dollar Value of 1 basis point) - $ change in bond price for 0.01% change in yields.')
# Find the duration of the bond
price = -npf.pv(rate=.05,nper =30,pmt =3.5,fv=100)
price_up = -npf.pv(rate=.06,nper =30,pmt =3.5,fv=100)
price_down = -npf.pv(rate=.04,nper =30,pmt =3.5,fv=100)
duration = (price_down - price_up)/ (2* price *.01)

# Find the dollar duration of the bond
dollar_duration = duration * price * .01
print("Dollar Duration: ", dollar_duration)

# Find the DV01 of the bond
dv01 = duration * price * .0001
print("DV01: ", dv01)


print('---------------------------------------Hedging')
#Say you own a portfolio of bonds whose combined DV01 is USD 5,000. You decide to hedge this portfolio by selling a fixed amount of the 30 year bond from the previous exercise, which has a price of USD 76.94 and a DV01 of 12.88 cents.

# Assign DV01 of portfolio and bond to variables
portfolio_dv01 = 5000
bond_dv01 = 0.1288
bond_price = 76.94

# Calculate quantity of bond to hedge portfolio
hedge_quantity = portfolio_dv01 / bond_dv01
print("Number of bonds to sell: ", hedge_quantity)

# Calculate dollar amount of bond to hedge portfolio
hedge_amount = hedge_quantity * bond_price
print("Dollar amount to sell: USD", hedge_amount)


print('------------------------Predicting price impacts from duration')
#The bond has a maturity of 5 years, coupon of 7%, yield of 4%, and face value of USD 100. It has a price of USD 113.36 and dollar duration of USD 4.83. You will predict the price change for a 2% decrease in interest rates.

# Assign bond price, dollar duration, yield change to variables
bond_price = 113.36
dollar_duration = 4.83
yield_change = -0.02

# Predict bond price change using duration
price_prediction = -100 * dollar_duration * yield_change
print("Predicted Change: USD ", price_prediction)

# Find actual price change and compare
price_actual = -npf.pv(rate=0.02, nper=5, pmt=7, fv=100) - bond_price
print("Actual Change: USD ", price_actual)
print("Estimation Error: USD ", price_prediction - price_actual)



print('-------------------Predicted vs. actual prices I')
# Price a 10 year bond with 5% coupon and 5% yield, reprice at higher and lower yields
price = -npf.pv(rate=0.05, nper=10, pmt=5, fv=100)
price_up = -npf.pv(rate=0.06, nper=10, pmt=5, fv=100)
price_down = -npf.pv(rate=0.04, nper=10, pmt=5, fv=100)

# Find the duration and dollar duration of the bond
duration = (price_down - price_up) / (2 * price * 0.01)
dollar_duration = duration * price * 0.01

# Create an array of yields from 0 to 10 in steps of 0.1, convert to DataFrame
bond_yields = np.arange(0, 10, 0.1)
bond = pd.DataFrame(bond_yields, columns=['bond_yield'])

# Add a column called price with the bond price for each yield level
bond['price'] = -npf.pv(rate=bond['bond_yield'] / 100, nper=10, pmt=5, fv=100)

# Add a column called yield_change with the current yield minus original yield
bond['yield_change'] = (bond['bond_yield'] - 5)

# Find the predicted bond price change using dollar duration then find predicted price
bond['price_change'] = -100 * dollar_duration * bond['yield_change'] / 100
bond['predicted_price'] = price + bond['price_change']

# Plot bond yields against predicted and actual prices, add labels, legend, and display
plt.plot(bond['bond_yield'], bond['price'])
plt.plot(bond['bond_yield'], bond['predicted_price'])
plt.xlabel('Yield (%)')
plt.ylabel('Price (USD)')
plt.title('Actual Bond Prices vs.Predicted Prices Using Duration')
plt.legend(["Actual Price", "Predicted Price"])
plt.show()


print('-------------------Using the curvature of the price/yield line')

# Create array of yields and convert to pandas DataFrame
bond_yields = np.arange(0, 20, 0.1)
bond = pd.DataFrame(bond_yields, columns=['bond_yield'])

# Add columns for 5 year and 20 year bonds
bond['price_5y'] = -npf.pv(rate=bond['bond_yield'] / 100, nper=5, pmt=5, fv=100)
bond['price_20y'] = -npf.pv(rate=bond['bond_yield'] / 100, nper=20, pmt=5, fv=100)

# Create plot for bond bonds, add labels to axes, legend, and display
plt.plot(bond['bond_yield'], bond['price_5y'])
plt.plot(bond['bond_yield'], bond['price_20y'])
plt.xlabel('Yield (%)')
plt.ylabel('Price (USD)')
plt.title('Plot a price/yield graph to see which bond has the greatest convexity.')
plt.legend(["5 Year Bond", "20 Year Bond"])
plt.show()


print('-------------------Plotting convexity vs. the factor')

# Create array of bond yields and covert to pandas DataFrame
bond_yields = np.arange(0, 20, 0.1)
bond = pd.DataFrame(bond_yields, columns=['bond_yield'])

# Find price of bond, reprice for higher and lower yields, calculate convexity
bond['price'] = -npf.pv(rate=bond['bond_yield'] / 100, nper=20, pmt=6, fv=100)
bond['price_up'] = -npf.pv(rate=bond['bond_yield'] / 100 + 0.01, nper=20, pmt=6, fv=100)
bond['price_down'] = -npf.pv(rate=bond['bond_yield'] / 100 - 0.01, nper=20, pmt=6, fv=100)
bond['convexity'] = (bond['price_down'] + bond['price_up'] - 2 * bond['price']) / (bond['price'] * 0.01 ** 2)

# Create plot of bond yields against convexity, add labels to axes, display plot
plt.plot(bond['bond_yield'], bond['convexity'])
plt.xlabel('Yield (%)')
plt.ylabel('Convexity')
plt.title('20 year bond,6% coupon :convexity of this bond for different levels of yields.')
plt.show()


print('------------------------------Dollar Convexity and Convexity adjustment')
# Find price of 10 year zero coupon bond with a 5% yield, shift yields, and reprice
price = -npf.pv(rate=0.05, nper=10, pmt=0, fv=100)
price_up = -npf.pv(rate=0.06, nper=10, pmt=0, fv=100)
price_down = -npf.pv(rate=0.04, nper=10, pmt=0, fv=100)

# Calculate convexity and dollar convexity of the bond
convexity = (price_down + price_up - 2 * price) / (price * 0.01 ** 2)
dollar_convexity = convexity * price * 0.01 ** 2

# Find the convexity adjustment and print the result
convexity_adjustment = 0.5 * dollar_convexity * 100 ** 2 * 0.01 ** 2
print("Convexity adjustment: ", convexity_adjustment)


print('--------------------------------------------Combining duration and convexity')
# Find the price of 7 year bond with 3% coupon and 4% yield, shift yields and reprice
price = -npf.pv(rate=0.04, nper=7, pmt=3, fv=100)
price_up = -npf.pv(rate=0.05, nper=7, pmt=3, fv=100)
price_down = -npf.pv(rate=0.03, nper=7, pmt=3, fv=100)

# Find duration and dollar duration of the bond
duration = (price_down - price_up) / (2 * price * 0.01)
dollar_duration = duration * price * 0.01

# Find convexity, dollar convexity and convexity adjustment
convexity = (price_down + price_up - 2 * price) / (price * 0.01 ** 2)
dollar_convexity = convexity * price * 0.01 ** 2
convexity_adjustment = 0.5 * dollar_convexity * 100 ** 2 * 0.01 ** 2

# Combine duration and convexity to predict bond price change
combined_prediction = -100 * dollar_duration * 0.01 + convexity_adjustment
print("Predicted Price Change: ", combined_prediction)