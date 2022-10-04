person1 = {
    "firstname": "aizhan",
    "lastname": "myrzakimova",
    "address": "111 n state"
}

print(person1.values())
print(person1.keys())

print("This persons firstname is", person1.get("firstname"))
print("This persons lastname is", person1.get("lastname"))
print("This persons address is", person1.get("address"))