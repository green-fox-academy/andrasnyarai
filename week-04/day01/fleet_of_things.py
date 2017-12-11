from fleet import Fleet
from thing import Thing

fleet = Fleet()

# You have the Thing class
# You have the Fleet class
# You have the fleet_of_things.py file
# Download those, use those
# In the fleet_of_things file create a fleet
# Achieve this output:


# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

milk = Thing('Get milk')
obstacle = Thing('Remove the obstacles')
stand_up = Thing('Stand up')
eat = Thing('Eat lunch')

stand_up.complete()
eat.complete()

fleet.add(milk)
fleet.add(obstacle)
fleet.add(stand_up)
fleet.add(eat)


print(fleet)