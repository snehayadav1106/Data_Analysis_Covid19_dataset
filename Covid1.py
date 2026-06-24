import matplotlib.pyplot as plt
import pandas as pd
import os



script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "country_wise_latest.csv")

df = pd.read_csv(csv_path)

# Top 10 countries by confirmed cases
top_countries = df.nlargest(10, 'Confirmed')['Country/Region'].tolist()
filtered_df = df[df['Country/Region'].isin(top_countries)]

# Plot bar chart
plt.figure(figsize=(10,6))
plt.bar(filtered_df['Country/Region'], filtered_df['Confirmed'], color='skyblue')

for i, value in enumerate(filtered_df['Confirmed']):
    plt.text(i, value + 2, str(value), ha='center')

plt.title('Top 10 Confirmed COVID Cases')
plt.xlabel('Country')
plt.ylabel('Confirmed Cases')
plt.xticks(rotation=45)
plt.show()