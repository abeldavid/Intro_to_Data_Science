#!python2
import sys
import pandas
import numpy
import scipy.stats

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

def compare_averages(filename):

    baseball_data = pandas.read_csv(filename)

    # Split the data into two data frames
    baseball_data_left = baseball_data[baseball_data['handedness'] == 'L']
    baseball_data_right = baseball_data[baseball_data['handedness'] == 'R']

    # Perform Welch's t-test

    result = scipy.stats.ttest_ind(baseball_data_left['avg'], baseball_data_right['avg'], equal_var = False)

    # Produce desired output
    if result[1] <= .05 :
        return (False, result)
    else:
        return (True, result)


if __name__ == "__main__":
    
    # Print the version of python used
    print (sys.version)
    
    # Path to csv file point to Master.csv
    path_to_csv = "C:/Users/David/Documents/Data/Research/2017/4_Sept_16_Data_Science/Scource_Code/Intro_to_Data_Science/Project_1/Data_Set/Master.csv"  
    
    # Path to csv file point to new_Master_with_nameFull.csv
    path_to_new_csv = "C:/Users/David/Documents/Data/Research/2017/4_Sept_16_Data_Science/Scource_Code/Intro_to_Data_Science/Project_1/new_Master_with_nameFull.csv"
    
    # Path to csv file point to baseball_stats.csv
    filename = "C:/Users/David/Documents/Data/Research/2017/4_Sept_16_Data_Science/Scource_Code/Intro_to_Data_Science/Project_4/Data_Set/baseball_stats.csv"  



    # Fills in the na values with the avg value of the weight column.
    #imputation(path_to_csv)

    # Function to add full name entry into the csv file
    #add_full_name(path_to_csv, path_to_new_csv)
 
    
    # Perform the t-Test
    result = compare_averages(filename)
    print result