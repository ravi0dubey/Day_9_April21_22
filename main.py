
Capital = {
  "France":"Paris"
 # "Germany":"Berlin",
 # "Italy":"Rome"
}

Vlog1 = {
  "France2":["Paris", "Nice","Deauville"]
  #"Germany":["Frankfurt","Berlin","Munich"],
  #"Italy":["Rome","Venice","Milan"]
}      

Vlog2 = {
  "France":{"Cities_Visited":["Paris","Nice","Deauville"],"No_of Visit" : [4,2,6]},
  "Germany":{"Cities_Visited":["Frankfurt","Berlin","Munich"],"No_of Visit" : [2,0,0]},
  "Italy":{"Cities_Visited":["Rome","Venice","Milan"],"No_of Visit" : [1,1,2]},
      }
#print(Vlog1)
#print(Vlog2)

#Vlog4 = {
# "Radha":{Vlog1}
#}
Vlog3 = [{"France":"Paris"}, {"France2":{"Cities_Visited":["Paris","Nice","Deauville"],"No_of Visit" : [4,2,6]},}
]

print(Vlog3)