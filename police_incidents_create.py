import os
import pandas as pd

# dataframe that contains the contents of all of the csv files
final_df = pd.DataFrame()
file_list = []

# location of the files that are going to be combined
folder = os.getcwd() + '/data/police_incidents/'
output = os.getcwd() + '/police_incidents_all_years.csv' 

# create list of file names
for file in os.listdir(folder):
    if file.endswith('.csv'):
        fullpath = folder + file 
        file_list.append(fullpath)

# combine files together
final_df = pd.concat(map(pd.read_csv, file_list))

# output the contents of the dataframe to final file
final_df.to_csv(output,index=False)