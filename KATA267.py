def itinerary(trips):
    route = []
    for segment in trips:
        if not route or route[-1] != segment['in']:
            route.append(segment['in'])
        route.append(segment['out'])
    return '-'.join(route)

