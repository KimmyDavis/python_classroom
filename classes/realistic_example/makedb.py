from person import Person, Manager

davis = Person("Davis Kimwera")
mars = Person("Mars Kampala", job="ui/ux", pay=1200)
sk = Manager("Sk Ok", pay=2400)

import shelve
db = shelve.open("person.db")
for object in (davis, mars, sk):
    db[object.name] = object
db.close()