#AMAZON ORDER DATA DOWNLOADED FROM INTERNET
#NOT REAL DATA, JUST AN ESTIMATE

import pandas as pd
ecom = pd.read_csv('Ecommerce Purchases')


# FIRST 5 ENTRIES
ecom.head()


# DATABASE INFO( NO OF ROWS, COLUMNS ETC)
ecom.info()


# Average purchase price
ecom['Purchase Price'].mean()


# HIGHEST & LOWEST PURCHASE PRICE
ecom['Purchase Price'].max()
ecom['Purchase Price'].min()


# NO. OF PEOPLE HAVING ENGLISH AS THEIR WEB LANGUAGE
ecom[ecom['Language']=='en'].count()

# PEOPLE HAVING JOB TITLE AS LAWYER
ecom[ecom['Job'] == 'Lawyer'].info()


# PEOPLE MAKING PURCHASE DURING AM OR PM
ecom['AM or PM'].value_counts()


# 5 MOST COMMON JOBS
ecom['Job'].value_counts().head(5)


# PRICE OF PURCHASE FROM LOT '90 WT'
ecom[ecom['Lot']=='90 WT']['Purchase Price']


# EMAIL OF PERSON MAKING PURCHASE WITH Credit Card Number: 4926535242672853
ecom[ecom["Credit Card"] == 4926535242672853]['Email'] 


# PEOPLE HAVING AMEX CARD & HAVING PURCHASE OVER 95$
ecom[(ecom['CC Provider']=='American Express') & (ecom['Purchase Price']>95)].count()


# CCs EXPIRING IN 2025
sum(ecom['CC Exp Date'].apply(lambda x: x[3:]) == '25')


# 5 MOST COMMON EMAIL PROVIDERS
ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5)

