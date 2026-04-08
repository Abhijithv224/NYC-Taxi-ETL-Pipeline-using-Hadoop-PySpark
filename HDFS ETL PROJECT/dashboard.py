import pandas as pd
import matplotlib.pyplot as plt

data = {
    "passenger_count": [1, 2, 3, 4],
    "revenue": [59, 13, 3, 1]
}

df = pd.DataFrame(data)

plt.bar(df["passenger_count"], df["revenue"])
plt.xlabel("Passenger Count")
plt.ylabel("Revenue")
plt.title("Revenue by Passenger Count")

plt.show()