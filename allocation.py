# read in data

volunteers = {} # dict of dict, name: {location: zip, availability:[time slots], distance_willing: max_dist}
donors = {} # dict of dict, name: {product: name, number: int, location: zip, availability:[time slots], transport_ability: bool, certified: bool, distance_willing: max_dist}
care_facilities = {} #dict of dict, name:{product: name, number: int, urgency: int, location: zip, transport_ability: bool, availability: [time slots], distance_willing: max_dist, certification_necessity: bool}

# remove fulfilled items from db once out of loop

# match donors who can transport to hospitals who cannot
for name, value in donors.items():
    if value['transport_ability']:
        max_dist_willing = value['max_dist']
        donor_location = value['location']


# match hospitals who can transport to donors who cannot


# match hospitals who can transport to donors who can


# match hospitals and donors who cannot transport with volunteers
