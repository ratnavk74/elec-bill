import sys

if len(sys.argv) == 2:
    units = float(sys.argv[1])
    print("User provided units:")
else:
    units = 100    
    print("No input provided — using default units:")

rate_per_unit = 5.0

bill_amount = units * rate_per_unit

print("\n----- ELECTRICITY BILL -----")
print("Units Consumed:", units)
print("Rate per Unit: ₹", rate_per_unit)
print("Total Bill: ₹", bill_amount)
