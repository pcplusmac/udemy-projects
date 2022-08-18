# this is the py file for project 201; refer to noteBook for the detail requirement on this project. 
# impor the package so thaT being able to make api requests
import requests

pokemon = input("input the name of the pokemon you want:")
pokemon = pokemon.lower()

url= f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
# make a request
req = requests.get(url)
print(type(req))

# validdate the data user input using 'if' statement, in case the data is not found in api database. 
if req.status_code==200:
    data=req.json()
    print(type(data))
    for ability in data['abilities']:
        print(f"ability is {ability['ability']['name']}\n url is : {ability['ability']['url']}")
else:
    print("data not found! enter new one")




