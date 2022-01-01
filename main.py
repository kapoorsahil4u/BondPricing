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

# Bond with price of USD 92 paying 3% coupon for 3 years
bond_a = npf.rate(nper=3, pmt=3, pv=-92, fv=100)
print("Bond A: ", bond_a)  # Since PV =92 Which is undervalued (or Discounted) hence its Yield is to be greater than Coupon rate

# Bond with price of USD 102 paying 6% coupon for 5 years
bond_b = npf.rate(nper=5, pmt=6, pv=-102, fv=100)
print("Bond B: ", bond_b)

# Bond with price of USD 95 paying 3% coupon for 5 years
bond_c = npf.rate(nper=5, pmt=3, pv=-95, fv=100)
print("Bond C: ", bond_c)
