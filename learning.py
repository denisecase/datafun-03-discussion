"""
How do students like to learn?

External libraries: wordcloud, matplotlib

wordcloud: used to generate wordclouds
matplotlib: used to plot the wordcloud

"""

# first, imports
import wordcloud 
import matplotlib.pyplot as plt

# Read text from file
with open("learning.txt", "r") as text_file:
  # read the entire file into a list of lines
  line_list = text_file.readlines()
  # we're at the end of the file after reading
  # so we need to reset the file pointer to the beginning
  # we'll seek() (move to) the 0th byte (character) in the file
  text_file.seek(0)
  # read the entire file into a single string
  long_string= text_file.read()
  # split the string into a list of words
  word_list = long_string.split()

# Summarize the text
print(f"There are {len(line_list)} lines in the file.")
print(f"There are {len(word_list)} words in the file.")
print("Be patient. ")
print("The figure (with muliple versions) may take a moment to appear.")
print("Could you make a new third version?")

width_px = 900
height_px = 600

# Use WordCloud to generate a wordcloud from the text
# set width and height to 800x400 pixels
wordcloud1 = wordcloud.WordCloud(width=width_px, height=height_px).generate(long_string)

# After exploring the original wordcloud, we found we could improve it
# There are many little words that didn't add much value
# Let's clean it up a bit, 
# Get read of less important words like "the", "and", "a"
# Use wordcloud to get a list of stopwords and use set get unique
stopwords_set = set(wordcloud.STOPWORDS)
# add a few stopwords of our own
stopwords_set.update('little','using','need','lot','stick','prefer', 'still')

# Try a second - better - wordcloud
wordcloud2 = wordcloud.WordCloud(
  width=width_px, 
  height=height_px,
  stopwords=stopwords_set,
  background_color='white',
  max_words=100,
).generate(long_string)

# Use Matplotlib.pyplot to plot the wordcloud
# since we have multiple charts, we'll use subplots
# creat the overall figure and set the size
# 10 inches wide, 8 inches tall
size_tuple_inches = (10,8)
# create figure 1
plt.figure(1, figsize=size_tuple_inches)

# create the first subplot
# 2 rows, 2 columns, this is the first chart
plt.subplot(221)
# plot the wordcloud using image show()
# pass in the wordcloud object
# pass in interpolation to make it look smoother
plt.subplot(221).imshow(wordcloud1, interpolation='bilinear')
# turn off the axis so they don't appear in the chart
plt.subplot(221).axis("off")
plt.subplot(221).set_title("Original Wordcloud")

# create the second subplot
# 2 rows, 2 columns, this is the second chart
plt.subplot(222).imshow(wordcloud2, interpolation='bilinear')
plt.subplot(222).axis("off")
plt.subplot(222).set_title("Improved Wordcloud")

# TODO: create a third wordcloud


# TODO: create a third subplot
# 2 rows, 2 columns, this is the third chart




# save the whole figure to a file
plt.savefig('learning.png', dpi = 100)
print("Saved. Showing figure. Can you add another? Hit Ctrl-C to quit.")

# show the whole figure
plt.show()

