
#USING SF SALARY DATA FROM KAGGLE
#(https://www.kaggle.com/kaggle/sf-salaries)

import pandas as pd

sal = pd.read_csv('Salaries.csv')
#Check the head of the DataFrame.
sal.head()
#Using the .info() method to find out how many entries there are
sal.info() # 148654 Entries

#Average BasePay ?
sal['BasePay'].mean()


#Highest Overtime Pay
sal['OvertimePay'].max()


# job  title of a "JOSEPH DRISCOLL"
sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']


# How much does he make, including benefits
sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']


# Highest paid employee
sal[sal['TotalPayBenefits']== sal['TotalPayBenefits'].max()]


# Lowest paid employee
sal[sal['TotalPayBenefits']== sal['TotalPayBenefits'].min()]


# Mean base pay per year
sal.groupby('Year').mean()['BasePay']


# Unique Jobs
sal['JobTitle'].nunique()


# Head of most common jobs
sal['JobTitle'].value_counts().head(5)


# Only 1 job per year
sum(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1)


# job title having word 'Chief' in it
def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False

sum(sal['JobTitle'].apply(lambda x: chief_string(x)))


# Relation between title length & job title?
sal['title_len'] = sal['JobTitle'].apply(len)
sal[['title_len','TotalPayBenefits']].corr()
