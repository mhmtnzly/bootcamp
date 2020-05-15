#%% Answer a
import pandas as pd

data=pd.read_excel("clinic_data.xlsx")
#print(type(data))
print("a) Data: \n",data)
#%% Answer b
print("b) Doctors Names:\n",data["doctor"])
#%% Answer c
print("c) From the 1st and 4th columns the 3rd to the 5th rows (inclusive):\n",data.iloc[2:5,[0,3]])
#%% Answer d
print("d) Year/Month/Patients:\n",data.loc[:,["year","month","patients"]])
#%% Answer e
print("e) Records from November:\n",data.loc[data["month"]=="November"])
#%% Answer f
print("f) Record with max patients:\n",data[data["patients"]==data["patients"].max()])
#%% Answer g
print("g) Records from September or February:\n",data[(data["month"]=="February") | (data["month"]=="September")])
#%% Answer h
print("h) Records after 2014 with fewer than 300 patients:\n",data[(data["year"]>2014)&(data["patients"]<300)])
#%% Answer i
print("i) Records from September or February with over 250 patients:\n"data[((data["month"]=="February") | (data["month"]=="September")) & (data["patients"]>250)])
#%% Answer j
data.set_index("doctor",inplace=True)
#%% Answer k
print("k) Year and Patients for Benitz and Carli:\n",data.loc[["Benitz","Carli"],["year","patients"]])



