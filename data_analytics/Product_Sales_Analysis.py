import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Order_Details = pd.read_csv(r"C:\Users\LENOVO\Downloads\Order_details(masked).csv")

# here we have taken Transaction
# date column
Order_Details['Time'] = pd.to_datetime(Order_Details['Transaction Date'])

# After that we extracted hour
# from Transaction date column
Order_Details['Hour'] = (Order_Details['Time']).dt.hour

# n =24 in this case, can be modified
# as per need to see top 'n' busiest hours
time_most1 = Order_Details['Hour'].value_counts().index.tolist()[:24]

time_most2 = Order_Details['Hour'].value_counts().values.tolist()[:24]

t_most = np.column_stack((time_most1, time_most2))

print(" Hour Of Day" + "\t" + "Cumulative Number of Purchases \n")
print('\n'.join('\t\t'.join(map(str, row)) for row in t_most))

time_most = Order_Details['Hour'].value_counts()
time_most1 = []

for i in range(0, 23):
    time_most1.append(i)

time_most2 = time_most.sort_index()
time_most2.tolist()
time_most2 = pd.DataFrame(time_most2)

plt.figure(figsize=(20, 10))

plt.title('Sales Happening Per Hour (Spread Throughout The Week)', fontdict={'fontname': 'monospace', 'fontsize': 30},
          y=1.05)

plt.ylabel("Number Of Purchases Made", fontsize=18, labelpad=20)
plt.xlabel("Hour", fontsize=18, labelpad=20)
plt.plot(time_most1, time_most2, color='m')
plt.grid()
plt.show()
