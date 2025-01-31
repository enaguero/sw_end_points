from .models import People, Planet
from .database import get_db

db_gen = get_db()  # Creates the generator
db = next(db_gen)   # Gets the session

# Planets
earth = Planet(name="Earth")
mars = Planet(name="mars")

# Add the instructions we would like to execute 
db.add(earth)
db.add(mars)

# We execute the actions
db.commit()

print("Earth ID :" , earth.id)
print("Earth representation: ", earth.__repr__())


resident1 = People(name="Francisco", last_name="Fernandez", email="student@4geeks.com", password="123123123", planet_id=earth.id)
resident2 = People(name="Javier", last_name="Pestana", email="ta@4geeks.com", password="123123123", planet_id = mars.id)

db.add(resident1)
db.add(resident2)

db.commit()
print("El residente de" , resident1.planet.name, "se llama", resident1.full_name())


