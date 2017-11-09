#!python2
import sys
import pandas
import numpy

def add_full_name(path_to_csv, path_to_new_csv):
    
    # Read the csv file as a panda dataframe
    baseball_data = pandas.read_csv(path_to_csv)
    
    # Print the first 5 rows
    #print(baseball_data.head())

    # Print the first 'nameFirst' Column
    #print baseball_data['nameFirst']
    
    # Concatenate the names  
    baseball_data['nameFull'] = baseball_data['nameFirst'] + ' ' + baseball_data['nameLast']
    
    # Write to new csvFile with the new entry 'nameFull
    baseball_data.to_csv(path_to_new_csv)


def imputation(filename):

    baseball = pandas.read_csv(filename)
    print baseball['weight']

    avg_weight = numpy.mean(baseball['weight'])
    print avg_weight

    baseball['weight'] = baseball['weight'].fillna(avg_weight)
    
    print baseball['weight']


if __name__ == "__main__":
    
    # Print the version of python used
    print (sys.version)
    
    # Path to csv file point to Master.csv
    path_to_csv = "C:/Users/David/Documents/Data/Research/2017/4_Sept_16_Data_Science/Scource_Code/Intro_to_Data_Science/Project_1/Data_Set/Master.csv"  
    
    # Path to csv file point to new_Master_with_nameFull.csv
    path_to_new_csv = "C:/Users/David/Documents/Data/Research/2017/4_Sept_16_Data_Science/Scource_Code/Intro_to_Data_Science/Project_1/new_Master_with_nameFull.csv"
    
    # Function to add full name entry into the csv file
    #add_full_name(path_to_csv, path_to_new_csv)

    #
    imputation(path_to_csv)