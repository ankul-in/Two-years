#kata
#https://www.codewars.com/kata/5899a4b1a6648906fe000113/train/python
# def find_routes(routes):
#     start=routes[0]
#     sequence=[start[0]]
#     while True:
#         for i in routes:
#                 if i[-1]==start[1]:
#                     sequence.append(i[-1])
#         return (sequence)
    
def find_routes(routes):
    route_map = {start: end for start, end in routes}
    start = routes[0][0]
    sequence = [start]

    while start in route_map:
        start = route_map[start]
        sequence.append(start)

    return sequence


print(find_routes([('MNL','TAG'), ('CEB','TAC'), ('TAG','CEB'), ('TAC','BOR')]))
print(find_routes([('Chicago','Winnipeg'), ('Halifax','Montreal'), ('Montreal','Toronto'), ('Toronto','Chicago'), ('Winnipeg','Seattle')]))