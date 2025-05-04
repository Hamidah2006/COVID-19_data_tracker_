# User-driven input (run in Notebook for interaction)
country = input("Enter a country (e.g., India): ")
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")

user_df = df[(df['location'] == country) & 
             (df['date'] >= start_date) & 
             (df['date'] <= end_date)]

# Plot new cases in that range
plt.figure(figsize=(10, 5))
plt.plot(user_df['date'], user_df['new_cases'], marker='o')
plt.title(f'New COVID-19 Cases in {country} from {start_date} to {end_date}')
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.grid(True)
plt.tight_layout()
plt.show()
