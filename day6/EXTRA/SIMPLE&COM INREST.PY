P = float(input("Enter Principal amount (P): "))
R = float(input("Enter Rate of Interest (R): "))
T = float(input("Enter Time in years (T): "))
SI = (P * R * T) / 100
CI = P*(1+R/100)^T-P
print("Simple Interest =", int(SI), int(CI))