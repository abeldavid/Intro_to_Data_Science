import pandas
from pandasql import sqldf
import pandasql as pdql
import sys




def select_first_50(path_to_csv, path_to_update_csv):
    
    # Read in our aadhaar_data csv to a pandas dataframe.  
    aadhaar_data = pandas.read_csv(path_to_csv)
    #print(aadhaar_data.head())
   
    # Rename the columns by replacing spaces with underscores and setting all characters to lowercase, so the
    # column names more closely resemble columns names one might find in a table.
    aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)
    #print(aadhaar_data.head())
    
    # Select out the first 50 values for "registrar" and "enrolment_agency"
    # in the aadhaar_data table using SQL syntax.
    # Note that "enrolment_agency" is spelled with one l. Also, the order
    # of the select does matter. Make sure you select registrar then enrolment agency
    # in your query.
    '''Example of query:

    q = """
    SELECT
    registrar, enrolment_agency
    FROM
    aadhaar_data
    LIMIT 50;
    """
    '''
 
    q = """
    SELECT
    gender, district, sum(aadhaar_generated) 
    FROM
    aadhaar_data
    WHERE age > 50 
    GROUP BY gender, district;
    """
    #Execute your SQL command against the pandas frame
    # The main function used in pandasql is sqldf. 
    # sqldf accepts 2 parametrs - a sql query string - an set of session/environment variables (locals() or globals())
    aadhaar_solution = pdql.sqldf(q.lower(), locals())
    print aadhaar_solution
    
    #Store aadhar_solution into new csv file
    #aadhaar_solution.to_csv(path_to_update_csv)   
if __name__ == "__main__":
    
    # Print the version of python used
    print (sys.version)
    
    # Path to csv file point to aadhar_data.csv
    path_to_csv = "C:/Users/David/Documents/Data/Research/2017/4_Sept_16_Data_Science/Scource_Code/Intro_to_Data_Science/Project_2/Data_Set/aadhaar_data.csv"  
    
    # Path to new csv file
    path_to_update_csv = "C:/Users/David/Documents/Data/Research/2017/4_Sept_16_Data_Science/Scource_Code/Intro_to_Data_Science/Project_2/new_aadhaar_data.csv"
    
    # Function to select first 50 entry from the csv file
    select_first_50(path_to_csv, path_to_update_csv)