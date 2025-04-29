import math;  # to compare our result with the real value

# 1️⃣ Get valid input from user
while True:
    try:
        x = float(input("Enter a value for x (must be between -1 and 1, not including -1 or 1): "))
            if -1 < x < 1:
                break
            else:
                print("Invalid input. x must be between -1 and 1 (exclusive). ")
            
            