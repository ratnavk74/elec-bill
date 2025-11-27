import sys

if len(sys.argv) == 1:
    units = float(sys.argv[1])
    print("User provided units:")
else:
    units = 100    
    print("No input provided — using default units:")

bill_amount = units * 0.5

print("\n----- ELECTRICITY BILL -----")
print("Units Consumed:", units)
print("Total Bill: ", bill_amount)
