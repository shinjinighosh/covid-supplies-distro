# Frontfacing
- Form for volunteers to add their availability - timing and location, and
  capacity (not just hospital resources but also groceries, essentials)
- Form for donors to add product, number and availability - timing and location,
  ability to transport/travel
- Form for hospitals/nursing homes/care facilities to ask for product, number,
  urgency, and location
- Form for storehouses to both add products, numbers and availability/location
  as well as space to store new items, and also if they have transportation
available
- Preview the current needs, if person had agreed to

# Backend
- simply put, match supply and demand
- collection: look at products donors are offering and match with volunteers,
  based on location nearness and common availability
- deposit: look at when a volunteer picks something up and match with a
  hospital/nursing home/care facility needing it, or a storehouse that can store
it
- matching: find volunteer (or use storehouse transportation) to match with
  hospitals' needs
- allocation: algorithm to choose which hospital receives how much, in times of
  overdemand and crisis

# Workflow
- on front screen, "I am..." + security
- frontfacing form to process running on the server which stores to a database
- database is csv file
- /magic matching works/
- every n hours (more frequent in daytime, hibernating overnight), depends on
  kind of product
- email them with matching:
    - volunteers get to know task
    - storehouses find out new storage, task, or which volunteer to expect to
    - donors find out who is coming when
    - hospitals find out what to expect when
    - storehouses find out new storage, task, or which volunteer to expect to
arrive with stuff, or gather stuff when
- update as done and remove completed tasks
- thank-yous and public facing impact update

# Products Offered
- essential medical supplies for covid
    - medicines
    - medical equipment: ventilator, disinfecting wipes, hand sanitizers, pap
      machines
- PPE
    - N95 masks
    - triple layer surgical masks
    - aprons
    - isolation gowns
    - face shields
    - surgical gloves
    - goggles
- food
- laboratory supplies
- essential non-covid medical supplies
- other essential supplies

# Data
- donors
    - product
    - number
    - location
    - times available to donate
    - ability to transport
    - distance willing to transport
    - certified?
- recipients
    - individuals
        - product
        - number
        - necessity
        - location
        - ability to transport
        - availability
        - certification necessity
    - hospitals/nursing homes/care facilities
        - product
        - number
        - urgency
        - location
        - ability to transport
        - distance willing to transport
        - availability
        - certification necessity
- tranport volunteers
    - availability
    - capacity for transportation
    - distance willing to transport
- storehouses
    - to donate
        - product
        - number
        - location
        - times available to donate
        - ability to transport
        - certified?
    - to store
        - space available (numbers per product)
        - location
        - times available to take in
        - ability to transport
    - to transport
        - availability
        - capacity for transportation
        - distance willing to transport
