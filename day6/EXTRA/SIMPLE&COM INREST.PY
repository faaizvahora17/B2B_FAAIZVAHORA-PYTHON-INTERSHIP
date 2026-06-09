P = float(input("Enter Principal amount (P): "))
R = float(input("Enter Rate of Interest (R): "))
N = float(input("Enter Time in years (T): "))
SI = (P * R * N) / 100
print(SI)
CI = P*(1+R/100)**N-P
print(CI)
print("Simple Interest =", int(SI), int(CI))