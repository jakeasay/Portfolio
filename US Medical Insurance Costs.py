import csv
import pandas as pd

data = pd.read_csv(r'/Users/jakeasay/Downloads/insurance.csv')
df = pd.DataFrame(data)
df.head()

def analyze_ages():
    total_age = df.age.mean()
    return ("Average Patient Age: " + str(round(total_age)) + " years")

def analyze_sexes():
    females = 0
    males = 0
    for sex in df.sex:
        if sex == 'female':
            females += 1
        elif sex == 'male':
            males += 1
    print("Count for female: ", females)
    print("Count for male: ", males)
    print('There are ' + str(males - females) + ' more males than females')

def unique_regions():
    unique_regions = []
    for region in df.region:
        if region not in unique_regions: 
            unique_regions.append(region)
    return unique_regions

def average_charges():
    total_charges = 0
    for charge in df.charges:
        total_charges += float(charge)
    return ("Average Yearly Medical Insurance Charges: " +  
        str(round(total_charges/len(df.charges), 2)) + " dollars.")

analyze_ages()

analyze_sexes()

unique_regions()

average_charges()

