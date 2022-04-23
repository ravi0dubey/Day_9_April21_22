Error_dictionary = {
  "Bug1":"Userid does not exist",
  "Bug2": "Userid and Password does not exist",
}

#print(Error_dictionary) # Print all contents of Dictionary
#print(Error_dictionary["Bug2"]) #Print value from Dictionary for Id = Bug2


#Error_dictionary["Bug1"] ="Userid not found" #Error Description of Bug1 gets updated 

#print(Error_dictionary) # Print all contents of Dictionary including updated content of Bug1
#print(Error_dictionary["Bug2"]) #Print value from Dictionary for Id = Bug2

Error_dictionary["Bug3"] ="Password is not strong" #Bug3 gets added to the list. 
Error_dictionary["Bug4"] = {"Userid should contain": ["Numbers","Alphabets","Symbols"], "Password should contain ":["Upper Case","LowerCase"]} #Error Description of Bug1 gets updated 
print(Error_dictionary) # Print all contents of Dictionary
#for Error_key in Error_dictionary:
#  print(Error_key) #It prints Bug1 and Bug2 which are the key of the Dictionary
#  print(Error_dictionary[Error_key]) #Error_Key act as subscript to print the content of Error_dictionary 
  
Error_dictionary = {} #Empty the Dictionary Content

print(Error_dictionary) # Print all contents of Dictionary

Capital = {"France":"Paris", "Germany":"Berlin","Italy":"Rome"}
Vlog = {
  "France":["Paris", "Nice","Deauville"],
  "Germany":["Frankfurt","Berlin","Munich"],
  "Italy":["Rome","Venice","Milan"]
       }
#for country in Vlog:
#  print(Vlog[country])

Vlog = {"France" : {"Cities_visited":["Paris","Nice","Deauville"], "total_visits": 12},
        "Germany": {"Cities_visited":["Frankfurt","Berlin","Munich"], "total_visits": 2},
        "Italy":{"Cities_visited":["Rome","Venice","Milan"], "total_visits": 5}}

#for country in Vlog:
#  print(Vlog[country])

country = "India"
Vlog[country]= {"Cities_visited":["Delhi","Mumbai","Chennai"], "total_visits": 15}

country = "Russia"
Vlog[country] = {"visits": 12,"cities": ["Paris", "Lille", "Dijon"], "aa": 16}
#print(Vlog)


order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {"Light": ["Burger", "Fries","Noodles"], "Heavy": ["Steak","Pizza"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"]["Light"][2-1]) 

order = {
    4: {1: "Salad", 2: "Soup"},
    2: {"Light": ["Burger", "Fries","Noodles"], "Heavy": ["Steak","Pizza"]},
    5: {3: ["Ice Cream"], 2: ["Rasogolla"]},
}

print(order[6-1][2][0]) #Exact Key Value should always be given like 3 or 2 to pick either of icecream or Rasogolla. It not positional based.   6-1 = 5 so it will point to 3rd key set pair. then we have 2 so it will go to list which has [Rasogolla].
# Within list we have given 0 as subscript so it will be pick Rasogolla. If we would have given [1] the it would have returned blank value.
               

Capital = {
  "France":"Paris"
 # "Germany":"Berlin",
 # "Italy":"Rome"
}

Vlog1 = {
  "France2":["Paris", "Nice","Deauville"],
  "Germany":["Frankfurt","Berlin","Munich"],
  "Italy":["Rome","Venice","Milan"]
}  
#Create Empty List A and initialize it with default value of 1
a= ["1"]
#fill a[0] with Data from Vlog1, 2nd element of Vlog1 which is ["Frankfurt","Berlin","Munich"]
a [0] = Vlog1["Germany"]

#Print  2nd element of Germany  which is "Berlin"
print(a[0][1])


Vlog2 = {
  "France":{"Cities_Visited":["Paris","Nice","Deauville"],"No_of Visit" : [4,2,6]},
  "Germany":{"Cities_Visited":["Frankfurt","Berlin","Munich"],"No_of Visit" : [2,0,0]},
  "Italy":{"Cities_Visited":["Rome","Venice","Milan"],"No_of Visit" : [1,1,2]},
      }
#It will print I visited Rome 1  times

print("I visited " + Vlog2["Italy"]["Cities_Visited"][0]  +" " +str(Vlog2["Italy"]["No_of Visit"][0]) +" times")


Vlog3 = [{"France":"Paris"}, {"France2":{"Cities_Visited":["Paris","Nice","Deauville"],"No_of Visit" : [4,2,6]},}
]

Vlog3[1]