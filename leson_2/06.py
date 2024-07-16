from decimal import Decimal, getcontext
getcontext().prec = 10
principal = 500000  
annual_rate = 8  
months = 24  

def EMI(P, annual_rate, n):
    P = Decimal(P)
    annual_rate = Decimal(annual_rate)
    n = Decimal(n)
    r = (annual_rate / 100) / 12
    
    emi = P * (r * (1 + r)**n) / ((1 + r)**n - 1)
    
    return emi

emi = EMI(principal, annual_rate, months)
print(f"Щомісячний платіж (EMI): {emi}")
