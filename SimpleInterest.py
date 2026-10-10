# # SI = P*T*R/100

# p = float(input("Enter principal amount : "))
# t = float(input("Enter time duration in years : "))
# r = float(input("Enter rate of interest : " ))

# si = (p*t*r) / 100

# print("Simple interest  : " , si)

def simple_interest(p,t,r):
    return (p*t*r)/ 100

p = float(input("Enter principal amount : " ))
t = float(input("Enter time duration in year : "))
r = float(input("Enter rate of interest : "))

si = simple_interest(p,t,r)
print("Simple interest is : ", si)