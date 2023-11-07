# Import Libraries
import pandas as pd 
from sklearn.naive_bayes import BernoulliNB

# Load the data
data = pd.read_csv("pdsep2023.csv")
print(data.head())

# Check and handle null data
print(data.isnull().sum())

# Feature and Target
feature = data[["Weather"]]
target = data["Play"]

# Check and handle cat data
nfeature = pd.get_dummies(feature)

print(feature)
print(nfeature)

# Model
model = BernoulliNB()
model.fit(nfeature, target)

# Predict
we = int(input("1 Overcast, 2 Rainy and 3 Sunny "))
if we == 1:
	d = [[1, 0, 0]]
elif we == 2:
	d = [[0, 1, 0]]
else:
	d = [[0, 0, 1]]

play = model.predict(d)
print(play)

# Internal working
res = model.predict_proba(d)
print(res)

info = res.ravel().tolist()
print(info)

pno = round(info[0]*100, 2)
pyes = round(info[1]*100, 2)
print("no = ", pno, "%")
print("yes = ", pyes, "%")
