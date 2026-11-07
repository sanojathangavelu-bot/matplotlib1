import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\acer\Downloads\Titanic.csv")
print(df.to_string())

x = np.array(["Survived", "Not Survived"])
y = np.array([(df["Survived"] == 1).sum(),(df["Survived"] == 0).sum()])
plt.title("Number of Passengers in Survived and Not Survived")
plt.xlabel("Survived Passengers")
plt.ylabel("Not Survived Passengers")
plt.bar(x,y)
plt.show()


