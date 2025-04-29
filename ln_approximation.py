import math  # to compare our result with the real value

# 1️⃣ Get valid input from user
while True:
    try:
        x = float(input("Enter a value for x (must be between -1 and 1, not including -1 or 1): "))
        if -1 < x < 1:
            break
        else:
            print("Invalid input. x must be between -1 and 1 (exclusive).")
    except ValueError:
        print("Please enter a valid number.")

# 2️⃣ Ask user whether they want to set a precision or max terms
choice = input("Do you want to specify a precision? (yes/no): ").strip().lower()

if choice == "yes":
    precision = float(input("Enter your desired precision (e.g., 0.000001): "))
    max_terms = 1000  # Just a safety cap so it doesn’t loop forever
else:
    precision = None
    max_terms = int(input("Enter maximum number of terms to use: "))

# 3️⃣ Start approximating ln(1 + x)
n = 1
term = x  # First term
total = 0.0
prev_total = 0.0
diff = float('inf')  # Start with an infinite diff to enter the loop

print("\nCalculating ln(1 + x) using series expansion...\n")
print(f"{'Term':<5}{'Value':>20}{'Running Total':>25}{'Difference':>20}")
print("="*70)

while n <= max_terms and (precision is None or diff >= precision):
    term = ((-1) ** (n + 1)) * (x ** n) / n
    total += term
    diff = abs(total - prev_total)

    print(f"{n:<5}{term:>20.10f}{total:>25.10f}{diff:>20.10f}")

    prev_total = total
    n += 1

# 4️⃣ Summary
actual = math.log(1 + x)
error = abs(actual - total)
print("\n" + "="*70)
print("Summary:")
print(f"Final approximation of ln(1 + x): {total:.10f}")
print(f"Exact value using math.log:     {actual:.10f}")
print(f"Number of terms used:           {n - 1}")
print(f"Difference from exact value:    {error:.10f}")
