import pandas as pd
from dataset import output_submission


partitions = 8
base_path = 'submissions/partition'
file_name = 'test2.csv'
team_name = 'RecSysCG'
contact_information = 'dimitreandrew@gmail.com'
joined_df = pd.read_csv(base_path + '%s.csv' % 0)

for i in range(1, partitions):
    df = pd.read_csv(base_path + '%s.csv' % i)
    joined_df = pd.concat([joined_df, df])

output_submission(joined_df, file_name, team_name, contact_information)
