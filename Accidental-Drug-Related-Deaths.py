import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# link to dataset and loading it using pandas library
dataset_url = 'https://code.datasciencedojo.com/datasciencedojo/datasets/raw/master/Accidental%20Drug%20Related' \
              '%20Deaths%20in%20Connecticut,%20US/Accidental%20Drug%20Related%20Deaths%20in%20Connecticut-2012-2018.csv'

dataset = pd.read_csv(dataset_url)

# which drugs are most associated with deaths

drugs = dataset.columns[21:38]
# print(drugs)
each_drug = dataset[drugs].apply(lambda col: col.value_counts().get('Y', 0))

# bar chart for "which drugs are most associated with deaths"
plt.figure(figsize=(12, 6))
sns.barplot(x=each_drug.index, y=each_drug.values)
plt.title("which drugs are most associated with deaths")
plt.xlabel("Type of the drug")
plt.ylabel("How many times found in dead body")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# finding if there are references in drug related deaths and gender
gender = dataset['Sex'].value_counts()

plt.figure(figsize=(10, 8))
sns.barplot(x=gender.index, y=gender.values)
plt.title("drug-related deaths by gender")
plt.xlabel("sex")
plt.ylabel("Deaths number")
plt.show()

# heatmap with deaths in cities and counties
cities_of_death = dataset["DeathCity"].value_counts()
counties_of_death = dataset["DeathCounty"].value_counts()

heatmap_data_city = dataset.groupby(['DeathCity', 'DeathCounty']).size().unstack(fill_value=0)

plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data_city, cmap='YlGnBu', annot=True, fmt='d', linewidths=.5)
plt.title('Distribution of Drug-Related Deaths Across Cities and Counties')
plt.xlabel('Death County')
plt.ylabel('Death City')
plt.show()

# deaths rate: hospital and residencies and other locations
locations = dataset[['Location', 'LocationifOther']]
location_categories = locations.apply(lambda row: 'Hospital' if row['Location'] == 'Hospital' else ('Residence' if row['Location'] == 'Residence' else 'Other'), axis=1)

location_counts = location_categories.value_counts()
total_deaths = len(dataset)
location_death_rates = location_counts / total_deaths * 100

plt.figure(figsize=(10, 8))
sns.barplot(x=location_death_rates.index, y=location_death_rates.values)
plt.title('Deaths by Location')
plt.xlabel('Location')
plt.ylabel('Percentage Death Rate')
plt.show()
