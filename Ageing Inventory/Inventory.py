import pandas as pd
import random
import datetime

itemID = []
for i in range(150):
    itemID.append(random.randint(100000,999999))

units_A = []
units_B = []
units_C = []
units_D = []
units_E = []
units_F = []
units_G = []
units_H = []
units_I = []
units_J = []
for i in range(150):
    units_A.append(random.randint(10,200))
    units_B.append(random.randint(10,200))
    units_C.append(random.randint(10,200))
    units_D.append(random.randint(10,200))
    units_E.append(random.randint(10,200))
    units_F.append(random.randint(10,200))
    units_G.append(random.randint(10,200))
    units_H.append(random.randint(10,200))
    units_I.append(random.randint(10,200))
    units_J.append(random.randint(10,200))


demand_A = []
demand_B = []
demand_C = []
demand_D = []
demand_E = []
demand_F = []
demand_G = []
demand_H = []
demand_I = []
demand_J = []
for i in range(150):
    demand_A.append(random.randint(10,150))
    demand_B.append(random.randint(10,150))
    demand_C.append(random.randint(10,150))
    demand_D.append(random.randint(10,150))
    demand_E.append(random.randint(10,150))
    demand_F.append(random.randint(10,150))
    demand_G.append(random.randint(10,150))
    demand_H.append(random.randint(10,150))
    demand_I.append(random.randint(10,150))
    demand_J.append(random.randint(10,150))

age_A = []
age_B = []
age_C = []
age_D = []
age_E = []
age_F = []
age_G = []
age_H = []
age_I = []
age_J = []
for i in range(150):
    age_A.append(random.randint(10,90))
    age_B.append(random.randint(10,90))
    age_C.append(random.randint(10,90))
    age_D.append(random.randint(10,90))
    age_E.append(random.randint(10,90))
    age_F.append(random.randint(10,90))
    age_G.append(random.randint(10,90))
    age_H.append(random.randint(10,90))
    age_I.append(random.randint(10,90))
    age_J.append(random.randint(10,90))
pred = [0]*150
Inventory = pd.DataFrame({'itemID':itemID,'Prediction':pred,'age_A':age_A,'demand_A':demand_A,'units_A':units_A,'age_B':age_B,'demand_B':demand_B,'units_B':units_B,'age_C':age_C,'demand_C':demand_C,'units_C':units_C,
'age_D':age_D,'demand_D':demand_D,'units_D':units_D,'age_E':age_E,'demand_E':demand_E,'units_E':units_E,'age_F':age_F,'demand_F':demand_F,'units_F':units_F,
'age_G':age_G,'demand_G':demand_G,'units_H':units_H,'age_H':age_H,'demand_H':demand_H,'units_H':units_H,'age_I':age_I,'demand_I':demand_I,'units_I':units_I,'age_J':age_J,'demand_J':demand_J,'units_J':units_J})


print(Inventory.head())
Inventory.to_csv('Inventory.csv',sep = ',', index = False)