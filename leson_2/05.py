from decimal import Decimal, getcontext
getcontext().prec = 10
def complex_interest(P, r, n, t):
    P = Decimal(P)
    r = Decimal(r)
    n = Decimal(n)
    t = Decimal(t)
    
    A = P * (1 + (r / n)) ** (n * t)
    
    return A
principal = 1000  # Основна сума (P)
annual_rate = 0.05  # Річна відсоткова ставка (r)
compounds_per_year = 4  # Кількість нарахувань відсотків на рік (n)
years = 10  # Кількість років (t)

amount = complex_interest(principal, annual_rate, compounds_per_year, years)

print(f"Сума після {years} років: {amount}")
