from pirates import Pirate, Captain, Ship

jack = Captain("Jack")
jack.drink_some_rum()

ghost_renoir = Ship("ghost renoir")
ghost_renoir.fill_ship(jack)

hubble = Captain("Hubble")
hubble.drink_some_rum()

white_denim = Ship("white denim")
white_denim.fill_ship(hubble)

ghost_renoir.mutiny('Coronado')

print(ghost_renoir.battle(white_denim))
print(ghost_renoir)

