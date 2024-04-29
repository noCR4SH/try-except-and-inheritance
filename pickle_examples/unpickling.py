import pickle

with open('data.pickle', 'rb') as file:
    data_loaded = pickle.load(file)

print(data_loaded)