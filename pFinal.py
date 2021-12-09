'''
Name: Oscar Andrade
Email: oscar.andrade08@myhunter.cuny.edu
Resources: https://numpy.org/doc/stable/reference/generated/numpy.linalg.matrix_power.html
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

#The data used was from NYC OpenData:
#https://data.cityofnewyork.us/Public-Safety/NYPD-Arrests-Data-Historic-/8h9b-rp9u/data
#https://data.cityofnewyork.us/Public-Safety/NYPD-Arrest-Data-Year-to-Date-/uip8-fykc/data

#NYPD-Arrests-Data-Historic 2018
input_file_ = "NYPD_Arrests_Data__Historic_2018.csv"
df_2018 = pd.read_csv(input_file_)

#NYPD-Arrests-Data-Historic 2019
input_file_1 = "NYPD_Arrests_Data__Historic_2019.csv"
df_2019 = pd.read_csv(input_file_1)

#NYPD-Arrests-Data-Historic 2020
input_file_2 = "NYPD_Arrests_Data__Historic_2020.csv"
covid_2020 = pd.read_csv(input_file_2)

def COUNT_NUMBER_OF_ARREST(df, column):
    result = len(df)
    return result

print(COUNT_NUMBER_OF_ARREST(covid_2020, 'ARREST_KEY')) #140413
print(COUNT_NUMBER_OF_ARREST(df_2019, 'ARREST_KEY')) #355030
print(COUNT_NUMBER_OF_ARREST(df_2018, 'ARREST_KEY')) #246773

def PERCENT_CHANGE(newNumber, oldNumber):
    value = 0
    percent = 0
    if newNumber < oldNumber:
        value = oldNumber - newNumber
        percent = (value / oldNumber)*100
    if newNumber > oldNumber:
        value = newNumber - oldNumber
        percent = (value / oldNumber)*100
    return value, percent

print(PERCENT_CHANGE(140413, 355030)) #2020 and 2019
print(PERCENT_CHANGE(140413, 246773)) #2020 and 2018

#counts the number of arrest by boro
def ARREST_BY_BORO(df, column):
    boros = []
    num_arrest = []

    result = df[column].value_counts()
    index = result.index

    for value in result:
        num_arrest.append(value)
    
    for boro in index:
        if boro == 'B':
            boros.append('Bronx')
        if boro == 'K':
            boros.append('Brooklyn')
        if boro == 'M':
            boros.append('Manhattan')
        if boro == 'Q':
            boros.append('Queens')
        if boro == 'S':
            boros.append('Staten_Island')

    return boros, num_arrest


boro, boroArrest = ARREST_BY_BORO(covid_2020, 'ARREST_BORO')
boro, boroArrest_2019 = ARREST_BY_BORO(df_2019, 'ARREST_BORO')
boro, boroArrest_2018 = ARREST_BY_BORO(df_2018, 'ARREST_BORO')

#graph only 2020 data
'''
plt.bar(boro, boroArrest_2019)
plt.title('NYPD Arrest By Boroughs')
plt.xlabel('Boroughs')
plt.ylabel('Number of Arrest')
plt.show()
'''

#graph 2020, 2019, 2018 data
X_axis = np.arange(len(boro))
  
plt.bar(X_axis, boroArrest, 0.25, label = '2020')
plt.bar(X_axis + 0.25, boroArrest_2019, 0.25, label = '2019')
plt.bar(X_axis + 0.25*2, boroArrest_2018, 0.25, label = '2018')

plt.xticks(X_axis+ 0.2, boro)
plt.title('NYPD Arrest By Boroughs')
plt.xlabel('Boroughs')
plt.ylabel('Number of Arrest')
plt.legend()
plt.show()


##########################################################################


#counts the number of arrest by race
def ARREST_BY_RACE(df, column):
    race = []
    num_arrest = []

    result = df[column].value_counts()
    index = result.index

    for value in result:
        num_arrest.append(value)
    
    for races in index:
        race.append(races)
    
    return race, num_arrest

races, raceArrest = ARREST_BY_RACE(covid_2020, 'PERP_RACE')
races, raceArrest_2019 = ARREST_BY_RACE(df_2019, 'PERP_RACE')
races, raceArrest_2018 = ARREST_BY_RACE(df_2019, 'PERP_RACE')

#graph only 2020 data
'''
fig = plt.figure(figsize =(50, 50))
plt.bar(races, raceArrest)
plt.title('NYPD Arrest By Race')
plt.xlabel('Race')
plt.ylabel('Number of Arrests')
plt.xticks(fontsize=12)
plt.show()
'''

#graph 2020, 2019, 2018 data
X_axis = np.arange(len(races))
  
plt.bar(X_axis, raceArrest, 0.25, label = '2020')
plt.bar(X_axis + 0.25, raceArrest_2019, 0.25, label = '2019')
plt.bar(X_axis + 0.25*2, raceArrest_2018, 0.25, label = '2018')

plt.xticks(X_axis+ 0.2, races)
plt.xlabel("Race")
plt.ylabel("Number of Arrest")
plt.title("NYPD Arrest By Race")
plt.legend()
plt.show()


##########################################################################


#counts the number of arrest throught out 2020
def count_month(df, column):
    January = 0
    February = 0
    March = 0
    April = 0
    May = 0
    June = 0
    July = 0
    August = 0
    September = 0
    October = 0
    November = 0
    December = 0
    for row in range(len(df)):
        date = df[column].iloc[row]
        month = datetime.datetime.strptime(date, "%m/%d/%Y").month
        if month == 1: 
            January += 1
        if month == 2: 
            February += 1
        if month == 3: 
            March += 1
        if month == 4: 
            April += 1
        if month == 5: 
            May += 1
        if month == 6: 
            June += 1
        if month == 7: 
            July += 1
        if month == 8: 
            August += 1
        if month == 9: 
            September += 1
        if month == 10: 
            October += 1
        if month == 11: 
            November += 1
        if month == 12: 
            December += 1

            
        
    return [January, February, March, April, May, June, July, August, September, October, November, December]

monthArrest = count_month(covid_2020, "ARREST_DATE")
monthArrest_2019 = count_month(df_2019, "ARREST_DATE")
monthArrest_2018 = count_month(df_2018, "ARREST_DATE")


print(monthArrest)
print(monthArrest_2019)
print(monthArrest_2018)
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#graph only 2020 data
'''
fig = plt.figure(figsize =(13, 7))
plt.plot(months, monthArrest)
plt.title('NYPD Arrest Throughtout 2020')
plt.xlabel('Year 2020')
plt.ylabel('Number of Arrests')
plt.show()
'''

#graph 2020, 2019, 2018 data
plt.plot(months, monthArrest, label = "2020")
plt.plot(months, monthArrest_2019, label = "2019")
plt.plot(months, monthArrest_2018, label = "2018")
plt.title('NYPD Arrest Throughtout 2020, 2019, 2018')
plt.xlabel('Months')
plt.ylabel('Number of Arrests')
plt.legend()
plt.show()
