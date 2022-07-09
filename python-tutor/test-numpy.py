import numpy as np

x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # เดือน
y=[25,35,40,42,51,60,62,72,78,90] # จำนวนสินค้าที่ขายได้ในแต่ละเดือน

x = np.array(x)
y = np.array(y)

x = x.reshape(-1, 1)

print(x)
print(y)