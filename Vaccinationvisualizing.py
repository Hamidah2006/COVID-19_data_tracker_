# Total vaccinations over time
plot_trend('total_vaccinations', 'Total Vaccinations Over Time', 'Total Vaccinations')

# Percentage vaccinated (optional calculation if available)
if 'people_fully_vaccinated_per_hundred' in df_filtered.columns:
    plot_trend('people_fully_vaccinated_per_hundred', 
               'Fully Vaccinated Population (%)', 'Percent Vaccinated')
  
