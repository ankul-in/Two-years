#greedy algorithm
# stations={}
# stations["kone"]=set(["id","nv","ut"])
# stations["ktwo"]=set(["wa","id","mt"])
# stations["kthree"]=set(["or","nv","ca"])
# stations["kfour"]=set(["nv","ut"])
# stations["kfive"]=set(["ca","az"])
# statesNeeded = set(["wa", "mt", "id", "nv", "ut", "or", "ca", "az"])
# finalStations=set()
# while statesNeeded:
#     bestStation=None
#     statesCovered=set()
#     for station,states in station.item():
#         covered=statesNeeded&states
#         if len(covered)>len(statesCovered):
#             bestStation=station
#             statesCovered=covered
#       finalStations.add(bestStation)
#       statesNeeded-=statesCovered
# print(finalStations)


stations = {
    "kone": set(["id", "nv", "ut"]),
    "ktwo": set(["wa", "id", "mt"]),
    "kthree": set(["or", "nv", "ca"]),
    "kfour": set(["nv", "ut"]),
    "kfive": set(["ca", "az"])
}

statesNeeded = set(["wa", "mt", "id", "nv", "ut", "or", "ca", "az"])
finalStations = set()

while statesNeeded:
    bestStation = None
    statesCovered = set()
    
    for station, states in stations.items():
        covered = statesNeeded & states
        if len(covered) > len(statesCovered):
            bestStation = station
            statesCovered = covered
    
    finalStations.add(bestStation)
    statesNeeded -= statesCovered

print("Selected stations:", finalStations)