import pickle

def store(var):
    pickle.dump(var, open("test.p", "wb"))

def read():
    reading = pickle.load(open("test.p", "rb"))
    print(reading)
    
choice = input("Read or write? ")
if choice.lower().startswith('r'):
    read()
elif choice.lower().startswith('w'):
    thing = input('String: ')
    store(thing)
