ishraq, clement, ishraq_dist, clement_dist = map(int, input().split())

possible_locations = [ishraq+ishraq_dist, ishraq-ishraq_dist, clement+clement_dist, clement-clement_dist]

for i in range(len(possible_locations)-1):
    location = possible_locations.pop(i)
    if location in possible_locations:
        print(location)
        break
    else:
        possible_locations.insert(i, location)
