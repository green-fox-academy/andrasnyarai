# Create a PostIt class that has
# a background_color
# a text on it
# a text_color
# Create a few example post-it objects:
# an orange with blue text: "Idea 1"
# a pink with black text: "Awesome"
# a yellow with green text: "Superb!"

class Post_it(object):

    def __init__(self,bg_color,text,text_color):
        self.bg_color = bg_color
        self.text = text
        self.text_color = text_color

post_it_one = Post_it("orange","Idea 1","blue")
post_it_two = Post_it("pink","Awesome","black")
post_it_three = Post_it("yellow","Superb","green")

print(post_it_one.bg_color + "|" + post_it_one.text + "|" + post_it_one.text_color)

