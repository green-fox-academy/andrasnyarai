# BlogPost
# - Create a `BlogPost` class that has
#   - an `author_name`
#   - a `title`
#   - a `text`
#   - a `publication_date`
# - Create a few blog Post objects:
#   - "Lorem Ipsum" titled by John Doe Posted at "2000.05.04."
#     - Lorem ipsum dolor sit amet.
#   - "Wait but why" titled by Tim Urban Posted at "2010.10.10."
#     - A popular long-form, stick-figure-illustrated blog about almost everything.
#   - "One Engineer Is Trying to Get IBM to Reckon With Trump" titled by William Turton at "2017.03.28."
#     - Daniel Hanley, a cybersecurity engineer at IBM, doesn�t want to be the center of attention. When I asked to take his picture outside one of IBM�s New York City offices, he told me that he wasn�t really into the whole organizer profile thing.


class BlogPost(object):

  def __init__(self, author_name, title, publication_date):
    self.text = ""
    self.author_name = author_name
    self.title = title
    self.publication_date = publication_date

  def add_text(self, new_strings):
    self.text += new_strings

  def __str__(self):
    return "AUTHOR {} | {} | {} | {}".format(self.author_name, self.title, self.text, self.publication_date)

  
blog_1 = BlogPost("John Doe", "Lorem Ipsum", "2000.05.04.")
  
blog_2 = BlogPost("Tim Urban", "Wait but why", "2010.10.10.")
  
blog_3 = BlogPost("William Turton", "One Engineer Is Trying to Get IBM to Reckon With Trump", "2017.03.28.")

blog_1.add_text('Lorem ipsum dolor sit amet.')

blog_2.add_text('A popular long-form, stick-figure-illustrated blog about almost everything.')

blog_3.add_text('''Daniel Hanley, a cybersecurity engineer at IBM,
doesn�t want to be the center of attention. When I asked to take
his picture outside one of IBM�s New York City offices, he told me 
that he wasn�t really into the whole organizer profile thing.''')

print(blog_3.author_name)
print('- ' + blog_3.title + ' -')
print(blog_3.text)
print('| ' + blog_3.publication_date + ' |')
