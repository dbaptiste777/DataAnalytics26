
contact_info = {
    "name": "Michael Jackson",
    "address": "456 Hehee Lane",
    "city": "Gary",
    "state": "Indiana",
    "zip": "07645"
}



print(f"""
{contact_info['name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}
""")

#Results Michael Jackosn 456 Hehee Lane Gary, Indiana 07645

contact_info.pop("name")
print(contact_info)

#Results {'address': '456 Hehee Lane', 'city': 'Gary', 'state': 'Indiana', 'zip': '07645'}

full_name = {
    "first name": "Michael",
    "last name": "Jackson"
}
print(full_name)

#Results {'skittles mango', 'lollipop strawberry', 'air heads cherry'}

full_name.update({"honorific": "Mr."})

print(full_name)

#Results {'first name': 'Michael', 'last name': 'Jackson', 'honorific': 'Mr.'}

contact_info.update({"full_name": full_name})


print(f"""
{contact_info['full_name']['honorific']} {contact_info['full_name']['first name']} {contact_info['full_name']['last name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}
""")

#Results Mr. Michael Jackson 456 Hehee Lane Gary, Indiana 07645
