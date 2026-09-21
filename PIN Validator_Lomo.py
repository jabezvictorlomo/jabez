# TITLE: PIN VALIDATOR
# AUTHOR: Lomo, Jabez Victor A.
# GRADE & SECTION: 8-Camia
pin = input("Enter your six-digit PIN: ")
if len(pin) == 6 and pin.isdigit():
    print("Valid PIN.")
else:
    print("Invalid PIN. Enter exactly 6 digits.")