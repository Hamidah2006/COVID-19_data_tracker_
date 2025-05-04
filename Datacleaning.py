# Filter selected countries
selected_countries = ['India', 'United States', 'Kenya']
df_filtered = df[df['location'].isin(selected_countries)]

# Fill missing numeric values with 0
df_filtered.fillna(0, inplace=True)

# Convert 'date' column (already done above) — included again for emphasis
df_filtered['date'] = pd.to_datetime(df_filtered['date'])

# Calculate death rate
df_filtered['death_rate'] = df_filtered['total_deaths'] / df_filtered['total_cases']
df_filtered['death_rate'] = df_filtered['death_rate'].fillna(0)
