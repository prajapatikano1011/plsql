salary=float(input("enter your salary:"))

hra=0.20 * salary
da=0.10 * salary
pf=0.12 * salary

gross_salary=salary+hra+da
net_salary=gross_salary-pf

print(f"hra={hra:.2f}")
print(f"da={da:.2f}")
print(f"pf={pf:.2f}")
print(f"gross salary={gross_salary:.2f}")
print(f"net salary={net_salary:.2f}")