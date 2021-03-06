import math
import numpy as np

# Example (annual compounding): what amount does $100
# invested at 10% (or 7%) per year for 7 (or 10) years grow to?


def compound_interest(principle, rate, time):

    # Calculates compound interest
    CI = principle * (pow((1 + rate / 100), time))
    # print("Compound interest is", CI)
    return np.round(CI, 5)


def monthly_compounding(principle, rate, month, year):
    CI = principle * (pow((1 + (rate / 100)/month), month*year))

    return np.round(CI, 2)


def calculate_compound_interest(p0, r, t):
    # List of final amounts.
    p = []
    for i in range(len(p0)):
        p.append(p0[i] * math.exp(r * t[i]))
    return p

def Continuous_compounding(principle, rate, time):
    CI = principle*np.exp((rate/100)*time)
    return np.round(CI, 4)

def Future_value(rate, nper, pmt, pv):
    investment = np.fv(rate, nper, pmt, pv)
    return investment
def Bond_yeld(principle, rate, time):
    for i in range(len(principle)):
        P += principle*np.exp(-rate*time)
    return P

print(calculate_compound_interest([1, 2, 3], 0.5, [1, 10, 100]))
# Driver Code
print(compound_interest(1, 10, 2))
print(compound_interest(100, 7, 10))
print(monthly_compounding(20000, 8.5, 12, 4))
print(Continuous_compounding(100, 5, 3))
print("Future value: ", Future_value(0.08, 15, 0,10000))