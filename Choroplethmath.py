# Get the most recent data
latest = df[df['date'] == df['date'].max()]

# Plot total cases by country
fig = px.choropleth(latest, locations="iso_code", color="total_cases",
                    hover_name="location", title="Total COVID-19 Cases by Country",
                    color_continuous_scale=px.colors.sequential.Plasma)
fig.show()

# Plot total vaccinations by country
fig2 = px.choropleth(latest, locations="iso_code", color="total_vaccinations",
                     hover_name="location", title="Total COVID-19 Vaccinations by Country",
                     color_continuous_scale=px.colors.sequential.Greens)
fig2.show()
