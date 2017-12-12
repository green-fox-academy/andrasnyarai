class Trees(object):

    def __init__(self,types,leaf_color,age,sex):
        self.type = types
        self.leaf_color = leaf_color
        self.age = age
        self.sex = sex

    def __str__(self):
        return "# {} # {} # {} # {}".format(self.type, self.leaf_color, self.age, self.sex)



pine = Trees("Pine","red","40","¤")
oak = Trees("Oak","yellow","76","~")
hazel = Trees("Hazel","brown","40","¤~")
elm = Trees("Elm","green","40","¤")

print(pine)
print(oak)
print(hazel)
print(elm)