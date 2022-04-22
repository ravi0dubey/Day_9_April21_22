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