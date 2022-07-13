import pandas as pd

# def f(x):
# 	k = 10*x + 5
# 	return k
#
# y = f(5)
# print(y)  #55


# def f(x):
# 	k = 10*x + 5
# 	print(k)
# y = f(5)
# print(y)  #55 none

#-----------------------------
#itertuples - pandas Dataframe row행 반복
dates=['April-10', 'April-11', 'April-12', 'April-13','April-14','April-16']
income1=[10,20,10,15,10,12]
income2=[20,30,10,5,40,13]
df=pd.DataFrame({"Date":dates, "Income_1":income1, "Income_2":income2})
for row in df.itertuples():
     print("Total income in "+ row.Date+ " is:"+str(row.Income_1+row.Income_2))
#-----------------------------
