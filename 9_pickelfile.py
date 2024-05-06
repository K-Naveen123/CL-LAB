import pickle

# Example data
data = {'key': 'value'}

# Save data to a file using Pickle
with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)

