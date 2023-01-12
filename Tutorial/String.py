print('''hallo everyone  
lets nacho nacho ''')

name = "Souze"
print(type(name))
# Concatenating two strings
greeting = "Good Morning, "
c = greeting + name
print(c)
print(name[4]) # can get by this
# name[3] = "d" --> Does not work / can't change by this

print(name[1:4])
print(name[:4]) # is same as name[0:4]
print(name[1:]) # is same as name[1:5]
c = name[-4:-1] # is same is name[1:4]
print(c)

name = "HarryIsGood"
# d = name[0::3] ---> start: end : increment(jump rhythm)
d = name[:0:-1]
print(d)

#[[[[[[[[[[[[[[ --Methods---]]]]]]]]]]]]]]

story = "once upon a time there was a youtuber named Harry who uploaded python course with notes Harry"

# print(len(story))
# print(story.endswith("notes")) --> is String end with the given string or not return boolean
# print(story.count("c")) ---> Cont how many times that character  present in that string------------ Also can pass the word for count 
# print(story.capitalize()) 
# print(story.find("upon"))  ----->return the index of that string where it find in that string
print(story.replace("Harry", "CodeWithHarry"))  #----> Change the original string and return the new string ------ 'whatWillChange', "withWhom"

