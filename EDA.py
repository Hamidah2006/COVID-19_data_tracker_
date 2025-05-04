# Define reusable plotting function
def plot_trend(metric, title, ylabel):
    plt.figure(figsize=(12, 6))
    for country in selected_countries:
        country_df = df_filtered[df_filtered['location'] == country]
        plt.plot(country_df['date'], country_df[metric], label=country)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Total cases over time
plot_trend('total_cases', 'Total COVID-19 Cases Over Time', 'Total Cases')

# Total deaths over time
plot_trend('total_deaths', 'Total COVID-19 Deaths Over Time', 'Total Deaths')

# New daily cases
plot_trend('new_cases', 'Daily New COVID-19 Cases Over Time', 'New Cases')

# Death rate over time
plot_trend('death_rate', 'COVID-19 Death Rate Over Time', 'Death Rate')
