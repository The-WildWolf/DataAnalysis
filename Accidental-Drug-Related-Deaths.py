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
plt.figure(figsize=(12,6))
sns.barplot(x=each_drug.index, y=each_drug.values)
plt.title("which drugs are most associated with deaths")
plt.xlabel("Type of the drug")
plt.ylabel("How many times found in dead body")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

