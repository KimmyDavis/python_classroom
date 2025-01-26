import shelve
db = shelve.open("person.db")
for key in sorted(db):
    print(key, "\t=>", db[key])

mars = db["Mars Kampala"]
mars.give_raise(0.1)
db["Mars Kampala"] = mars
db.close()
