import pandas as pd

# link to dataset and loading it using pandas library
dataset_url = 'https://code.datasciencedojo.com/datasciencedojo/datasets/raw/master/Accidental%20Drug%20Related' \
              '%20Deaths%20in%20Connecticut,%20US/Accidental%20Drug%20Related%20Deaths%20in%20Connecticut-2012-2018.csv'

dataset = pd.read_csv(dataset_url)



