contacts = [
    {
        "name": "Jonnathon",
        "phone": "98765 12345",
        "conversations": [
                            "hi",
                            "Hello",
                            "This is awesome day",
                            "Lets go and play"
                         ]
    },
    {
        "name": "Fionna",
        "phone": "99811 22112",
        "conversations": [
            "hola",
            "Whats up",
            "I am good",
            "How's your day"
        ]
    },
    {
        "name": "George",
        "phone": "77651 11221",
        "conversations": [
            "heya",
            "lets go for a WALK",
            "Wow. Lets catch up",
            "thanks"
        ]
    }
]

search = input("Enter Keyword To Search: ")
print(search)

for contact in contacts:
    if contact["name"].lower().find(search.lower())>=0 or contact["phone"].find(search)>=0:
        print(contact)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``")