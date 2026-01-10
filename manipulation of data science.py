import pandas as pd

mydata={
    'cars': ['Toyota', 'Honda', 'Ford', 'BMW', 'Audi'],
    'speed': [120, 130, 125, 150, 160],
}
df = pd.DataFrame(mydata)
print(df)
df.loc[0:10]
df.loc[0:2]
list1 = ['pizza', 'burger', 'pasta', 'french fries', '']
df1 = pd.Series(list1, index=['a', 'b', 'c', 'd', 'e'])
print(df1)
list2 = [1, 2, 3, 4, 5]
df2 = pd.Series(list2, index = ['a', 'b', 'c', 'd', 'e'])
print(df2)
mydata={
    'cars': ['Toyota', 'Honda', 'Ford', 'BMW', 'Audi'],
    'speed': [120, 130, 125, 150, 160],
}
list1 = [x for x in range(1, 5)]
df3 = pd.DataFrame(mydata, list1)
print(df3)