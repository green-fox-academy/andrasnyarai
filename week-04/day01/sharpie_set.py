# Reuse your Sharpie class
# Create SharpieSet class
# it contains a list of Sharpie
# count_usable() -> sharpie is usable if it has ink in it
# remove_trash() -> removes all unusable sharpies

from sharpie import Sharpie

Sharpies = [["red",1.2,20],["blue",1.5,0],["yellow",2.0,0]]


pen_1 = Sharpie(Sharpies[0][0], 2.0)

print(pen_1.color)

class SharpieSet(object):
    Sharpiez = [["red",1.2,50],["blue",1.5,90],["yellow",2.0,0]]

    def count_usable(self):
        count = 0
        for i in range(len(self.Sharpiez)):
            if self.Sharpiez[i][2] > 0:
                count += 1
        return count

    def remove_trash(self):
        index = 0
        while index in range(len(self.Sharpiez)):
            if self.Sharpiez[index][2] == 0:
                self.Sharpiez.remove(self.Sharpiez[index])
            else:
                index += 1
        return self.Sharpiez



a_set = SharpieSet()

print(a_set.count_usable())

print(a_set.remove_trash())

