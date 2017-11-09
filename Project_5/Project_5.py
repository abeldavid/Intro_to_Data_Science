# import files
import sys
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics


def compute_cost(features, values, theta):
    """
    Compute the cost of a list of parameters, theta, given a list of features 
    (input data points) and values (output data points).
    """
    m = len(values)
    sum_of_square_errors = numpy.square(numpy.dot(features, theta) - values).sum()
    cost = sum_of_square_errors / (2*m)

    return cost

def Linear_Regression_FN(feature, values,sel):

    X = baseball_data[feature]
    
    #X.head()
    #print type(X)
    print X.shape
     
    y = baseball_data[values]
    
    print y.shape
    
    
    # Spliting X & y into Training and Testing Set
    
    X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=1)
    
    print("Data split into Training Set and Testing Set")
    
    

        print("Training Data")
        #print X_train.shape
        #print y_train.shape
        linreg = LinearRegression()
        linreg.fit(X_train,y_train)
        print linreg.intercept_
        print linreg.coef_
        zip(feature,linreg.coef_)
        
        print("Testing Data")
        y_pred = linreg.predict(X_test)
        
        
        print("Evaluate")
        print("A")
        print metrics.mean_absolute_error(y_test,y_pred)
        print("B")
        print metrics.mean_squared_error(y_test,y_pred)
        print("C")
        print np.sqrt(metrics.mean_squared_error(y_test,y_pred))
        print("D")
        compute_r_squared(y_test,y_pred)
        
def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.

    # YOUR CODE GOES HERE
    SST = ((data-np.mean(data))**2).sum()
    SSReg = ((predictions-data)**2).sum()    
    r_squared = 1 - SSReg /SST
    print r_squared        



if __name__ == "__main__":
    
    # Print the version of python used
    print (sys.version)
    
    # Path to csv file point to baseball_stats-csv.csv
    path_to_csv = "C:/Users/David/Documents/Data/Research/2017/4_Sept_16_Data_Science/Scource_Code/Intro_to_Data_Science/Project_5/Data_Set/baseball_stats-csv.csv"  
    

    # Read the csv file as a panda dataframe
    baseball_data = pd.read_csv(path_to_csv)
    #Other attributes can be added to the .read_csv given below
    #header=0, engine = 'python', converters = {'name': str,'handedness': str,'height': np.int64,'weight': np.int64, 'avg': np.float64, 'HR':np.int64})
    #baseball_data['height'] = baseball_data['height'].astype(np.int64)
    #baseball_data['weight'] = baseball_data['weight'].astype(int64)
  
    #print baseball_data.dtypes 
    
    # Plot data
    #sns.pairplot(baseball_data, x_vars = ['height','weight'],y_vars = ['HR'], size= 10, aspect = 1, kind= 'reg')
    
    #print type(baseball_data['avg'][0])

    # Seperating Features
    feature = ['height','weight']
    #print type(feature)
    
    # Assigning values
    values =  ['HR']
    
    Linear_Regression_FN(feature , values ,1)   
    
