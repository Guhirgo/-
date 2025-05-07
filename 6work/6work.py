from  pprint import pprint

#
 # creation
user = {
    'id': 22,
    'name': "Alex",
    "hobbies": ["tenis", "socer"],
    "is_married": True,
    'address': {
        "citi": "Odesa",
        "strit": "Derebasib"
    },
    "siblings": None,
    'money' : 100,
}
user2= dict(id=365, name="John")
user3= dict(id=365, name="Mart", hobbies= None )

# parcel = {}
# parcel2 = dict()
#
# # # get data
# # user_id = user["id"]
# # user2_id = user2["id"]
# #
# #
# # user_hobbies = user.get("hobbies") or []
# # user2_hobbies = user2.get("hobbies") or []
# # user3_hobbies = user3.get("hobbies") or []
#
#
# # for hobby in user_hobbies:
# #     print(f"user hobby - {hobby}")
# #
# # for hobby2 in user2_hobbies:
# #     print(f"user hobby - {hobby2}")
#
# # updete
# # list type
# user2["hoddies"]=["diving"]
# user2["hoddies"]=["scuba"]
# user2["hoddies"].append("diving")
# # int typ
# user['money']= 200
#
# user['address']["citi"] = "lviv"
# user['address']["strit"] = "Colom"
#
# pprint(user, indent=4)

user_address = {
        "citi": "Odesa",
        "strit": "Derebasib",
    }
user_data = {
    "id": 18 ,
    "citi": "Kyiv",
}


result_dict_option1 = {**user_address, **user_data}
result_dict_option2 = user_address | user_data


# delet

result_dict_option1.clear()
# for elem in user:
#     print(elem,"->", user[elem])
atlet = []
for elem in user.values():
    atlet.extend(elem)



pass

