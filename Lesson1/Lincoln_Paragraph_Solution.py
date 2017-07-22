president = "abraham lincoln"
birth_month = 2
birth_day = 12
birth_year = 1809
last_words = "She won't think anything about it."

assassin = "JOHN WILKES BOOTH"

# Print the following with one print statement. Use only one variable for each line. Remember to comment your code and
# abide by the naming conventions for variables
#
# Here are some facts about Abraham Lincoln's life:
#       He was born 2/12/1809
#       He was the 16th president of the United States of America
#       He was assassinated by John Wilkes Booth
#       His last words were: "She won't think anything about it."

# Create a variable for to hold the content for line 1

line1 = "Here are some facts about " + president.title() + "\'s life:"

# Create a variable for to hold the content for line 2

line2 = "He was born " + str(birth_month) + "/" + str(birth_day) + "/" + str(birth_year)

# Create a variable for to hold the content for line 3

line3 = "He was the 16th president of the United States of America"

# Create a variable for to hold the content for line 4

line4 = "He was assassinated by " + assassin.title()

# Create a variable for to hold the content for line 5

line5 = "His last words were \"" + last_words + "\""

# Combine all lines for a final print statement

print(line1 + "\n\t" + line2 + "\n\t" + line3 + "\n\t" + line4 + "\n\t" + line5)