# TITLE: PAYMENT METHOD CHECKER
# AUTHOR: Lomo, Jabez Victor A.
# GRADE & SECTION: 8-Camia
valid_payments = ["cash","gcash", "card"]

payment = input(f"Please enter your payment method: ").lower()

if payment in valid_payments:
    print(f"Valid payment method.")
else:
    print(f"Invalid payment method.")