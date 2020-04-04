# Frontfacing
- Form for volunteers to add their availability - timing and location, and
  capacity (not just hospital resources but also groceries, essentials)
- Form for donors to add product, number and availability - timing and location
- Form for hospitals/nursing homes/care facilities to ask for product, number,
  urgency, and location
- Form for storehouses to both add products, numbers and availability/location
  as well as space to store new items, and also if they have transportation
available

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
    - donors find out who is coming when
    - hospitals find out what to expect when
    - storehouses find out new storage, task, or which volunteer to expect to
arrive with stuff, or gather stuff when
- update as done and remove completed tasks
- thank-yous and public facing impact update
