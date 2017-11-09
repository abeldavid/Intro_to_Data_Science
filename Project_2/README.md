# Project_2: How to work on SQL Query on python using PANDASQL.

# Note:
1.Lambda functions
 While normal functions are defined using the def keyword, in Python anonymous functions are defined using the lambda keyword.Hence, anonymous functions are also called lambda functions.
 Syntax
        lambda arguments: expression
  Eg:
     double = lambda x: x * 2
     # Output: 10
     print(double(5))

# Data Set :

The dataset (csv-file format) we are using can be downloaded from https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/aadhaar_data.csv containing the aadhaar data that we are passing.


# Objective:
    # Write a query that will select from the aadhaar_data table how many men and how 
    # many women over the age of 50 have had aadhaar generated for them in each district.
    # aadhaar_generated is a column in the Aadhaar Data that denotes the number who have had
    # aadhaar generated in each row of the table.
    #
    # The SQL query keywords are case sensitive. 
    # For example, if you want to do a sum make sure you type 'sum' rather than 'SUM'.
    #

    # The possible columns to select from aadhaar data are:
    #     1) registrar
    #     2) enrolment_agency
    #     3) state
    #     4) district
    #     5) sub_district
    #     6) pin_code
    #     7) gender
    #     8) age
    #     9) aadhaar_generated
    #     10) enrolment_rejected
    #     11) residents_providing_email,
    #     12) residents_providing_mobile_number




# Output:

PS C:\Users\David\Documents\Data\Research\2017\4_Sept_16_Data_Science\Scource_Code\Intro_to_Data_Science\Project_2> Py -2 Project_2.py

<O/P 1>
<OLD DATA>
        Registrar             Enrolment Agency             State    District  \
0  Allahabad Bank            Tera Software Ltd         Jharkhand      Ranchi
1  Allahabad Bank            Tera Software Ltd         Jharkhand      Ranchi
2  Allahabad Bank  Vakrangee Softwares Limited           Gujarat       Surat
3  Allahabad Bank  Vakrangee Softwares Limited  Himachal Pradesh      Kangra
4  Allahabad Bank  Vakrangee Softwares Limited    Madhya Pradesh  Chhindwara

  Sub District Pin Code Gender  Age  Aadhaar generated  Enrolment Rejected  \
0       Namkum   834003      M   63                  0                   1
1       Ranchi   834004      F   36                  0                   1
2        Nizar   394380      M   10                  1                   0
3     Baijnath   176081      M   44                  1                   0
4    Pandhurna   480334      M   35                  1                   0

   Residents providing email  Residents providing mobile number
0                          0                                  1
1                          0                                  1
2                          0                                  0
3                          1                                  1
4                          0                                  0

<NEW DATA>
        registrar             enrolment_agency             state    district  \
0  Allahabad Bank            Tera Software Ltd         Jharkhand      Ranchi
1  Allahabad Bank            Tera Software Ltd         Jharkhand      Ranchi
2  Allahabad Bank  Vakrangee Softwares Limited           Gujarat       Surat
3  Allahabad Bank  Vakrangee Softwares Limited  Himachal Pradesh      Kangra
4  Allahabad Bank  Vakrangee Softwares Limited    Madhya Pradesh  Chhindwara

  sub_district pin_code gender  age  aadhaar_generated  enrolment_rejected  \
0       Namkum   834003      M   63                  0                   1
1       Ranchi   834004      F   36                  0                   1
2        Nizar   394380      M   10                  1                   0
3     Baijnath   176081      M   44                  1                   0
4    Pandhurna   480334      M   35                  1                   0

   residents_providing_email  residents_providing_mobile_number
0                          0                                  1
1                          0                                  1
2                          0                                  0
3                          1                                  1
4                          0                                  0

<O/P 2>
    gender           district  sum(aadhaar_generated)
0        F         Ahmadnagar                      45
1        F        Ahmed Nagar                       0
2        F          Ahmedabad                       1
3        F              Ajmer                      27
4        F              Akola                       5
5        F          Alirajpur                      71
6        F          Allahabad                      15
7        F              Alwar                      14
8        F             Ambala                       7
9        F           Amravati                       0
10       F           Amritsar                      30
11       F            Anuppur                     101
12       F        Ashok Nagar                       1
13       F         Aurangabad                      19
14       F           Balaghat                     287
15       F          Bangalore                     433
16       F    Bangalore Rural                       9
17       F              Banka                       0
18       F           Banswara                      28
19       F              Baran                       5
20       F            Barwani                      34
21       F           Bathinda                      43
22       F               Beed                      25
23       F            Belgaum                      59
24       F            Bellary                      65
25       F              Betul                      41
26       F          Bhagalpur                       0
27       F           Bhandara                       4
28       F          Bharatpur                      94
29       F           Bhilwara                      50
..     ...                ...                     ...
498      M              Sirsa                     158
499      M            Solapur                      80
500      M          Sonbhadra                       7
501      M            Sonipat                      14
502      M        South Delhi                       5
503      M      South Tripura                       0
504      M   South West Delhi                       4
505      M  Sri Muktsar Sahib                      21
506      M         Tarn Taran                     125
507      M              Thane                     144
508      M          Tikamgarh                     265
509      M     Tiruvannamalai                       1
510      M               Tonk                      49
511      M             Tumkur                       1
512      M            Udaipur                      16
513      M             Ujjain                      66
514      M             Umaria                     137
515      M                Una                       3
516      M             Valsad                       2
517      M            Vellore                       0
518      M            Vidisha                      84
519      M         Viluppuram                      18
520      M             Wardha                       1
521      M             Washim                      33
522      M         West Delhi                       3
523      M     West Singhbhum                     227
524      M       West Tripura                      24
525      M             Yadgir                      12
526      M       Yamuna Nagar                     149
527      M           Yavatmal                      54