myDict = {
    "fast": "In a Quick Manner",
    "harry": "A Magician",
    "marks": [1, 2, 5],
    "Car": {"sportCar": "Player"},
    1: 2,
}
"""
Dict type is Key value pairs like object..
not Orderable but can Access by key
modification able after creation

as Value can Enter any type {string, int, list, dict}
key can't be multiple , if happen then one will be overwrite 
value can be same with different keys
"""

a = {}  # In this way declare Empty dict
# =============== method =================

print(myDict["fast"])  # Access through keys
myDict["Marks"] = [45, 78]  # update the Key values
print(myDict["Car"]["sportCar"])  # Access key of key --> get value

# Dictionary Methods
print((myDict.keys()))  # Prints the keys of the dictionary
# Prints the keys of the dictionary give in a list[]
print(list(myDict.keys()))
print(myDict.values())  # Prints the keys of the dictionary
print(
    myDict.items()
)  # Prints the (key, value) for all contents of the dictionary  --- [(key value pairs)]
print(myDict)  # same Just prints same { key : value }
updateDict = {
    "Sonia": "girl-Friend",
    "Hagimaru": "Friend",
    "Shubham": "Friend",
    "Aisha": "A Dancer",
}
myDict.update(
    updateDict
)  # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(
    myDict.get("Garry")
)  # Prints value associated with key "Garry" ---> If Key does not exist then it SHOWS NONE
print(
    myDict["keven"]
)  # Prints value associated with key "keven"  ---> If Key does not exist then it PRODUCE AN ERROR
