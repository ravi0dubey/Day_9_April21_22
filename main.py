Error_dictionary = {
  "Bug1":"Userid does not exist",
  "Bug2": "Userid and Password does not exist",
}

print(Error_dictionary) # Print all contents of Dictionary
print(Error_dictionary["Bug2"]) #Print value from Dictionary for Id = Bug2

Error_dictionary["Bug1"] ="Userid not found" #Error Description of Bug1 gets updated 

print(Error_dictionary) # Print all contents of Dictionary including updated content of Bug1
print(Error_dictionary["Bug2"]) #Print value from Dictionary for Id = Bug2

Error_dictionary["Bug3"] ="Password is not strong" #Bug3 gets added to the list. 

for Error_key in Error_dictionary:
  print(Error_key) #It prints Bug1 and Bug2 which are the key of the Dictionary
  print(Error_dictionary[Error_key]) #Error_Key act as subscript to print the content of Error_dictionary 
  
