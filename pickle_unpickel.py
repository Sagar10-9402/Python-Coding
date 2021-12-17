import pickle
cars=['swift','inova,farari']
file='cars1.pkl'
fileobj=open(file,'wb')
cars=pickle.dump(cars,fileobj)

file='cars1.pkl'
fileobj=open(file,'rb')
cars=pickle.load(fileobj)
print(cars)

