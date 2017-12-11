# Reuse your BlogPost class
# Create a Blog class
# list of BlogPosts
# add BlogPosts to your list
# delete(int) one item at given index
# update(int, BlogPost) one item at the given index and update it with another BlogPost

from blog_post import BlogPost

class Blog(object):

    def __init__(self,):
        self.list_of_blogposts = []

    def add_page(self,article):
        self.list_of_blogposts.append(article)
    
    def delete(self,number):
        del(self.list_of_blogposts[number])

    def update(self, number, new_post):
        self.list_of_blogposts[number] = new_post

    def __str__(self):
        result = ""
        for i in range(0, len(self.list_of_blogposts)):
            result += str(i+1) + ". " + self.list_of_blogposts[i].__str__() + "\n"
        return result

my_blog = Blog()

blog_1 = BlogPost("John Doe", "Lorem Ipsum", "2000.05.04.")
  
blog_2 = BlogPost("Tim Urban", "Wait but why", "2010.10.10.")
  
blog_3 = BlogPost("William Turton", "One Engineer Is Trying to Get IBM to Reckon With Trump", "2017.03.28.")

blog_1.add_text('Lorem ipsum dolor sit amet.')

blog_2.add_text('A popular long-form, stick-figure-illustrated blog about almost everything.')

blog_3.add_text('''Daniel Hanley, a cybersecurity engineer at IBM,
doesn�t want to be the center of attention. When I asked to take
his picture outside one of IBM�s New York City offices, he told me 
that he wasn�t really into the whole organizer profile thing.''')

blog_4 = BlogPost("Ra's al Ghul", "Burn London to the ground", "2017.12.12.")
blog_4.add_text("K I L L I T W I T H F I R E !")

my_blog.add_page(blog_1)
my_blog.add_page(blog_2)
my_blog.add_page(blog_3)

my_blog.delete(1)
my_blog.update(0,blog_4)
print(my_blog)