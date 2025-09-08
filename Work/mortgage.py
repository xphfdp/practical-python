# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month += 1
    if extra_payment_start_month <= month <= extra_payment_end_month:
        if principal * (1 + rate / 12) >= payment + extra_payment:
            principal = principal * (1 + rate / 12) - payment - extra_payment
            total_paid = total_paid + payment + extra_payment
        else:
            total_paid += principal * (1 + rate / 12)
            principal = 0
    else:
        if principal * (1 + rate / 12) >= payment:
            principal = principal * (1 + rate / 12) - payment
            total_paid = total_paid + payment
        else:
            total_paid += principal * (1 + rate / 12)
            principal = 0
    print(f"{month} {total_paid:.2f} {principal:.2f}")

print(f"Total paid {total_paid:.2f}\nMonths {month}")
