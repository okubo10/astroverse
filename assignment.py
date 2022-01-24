#  Join the items of this list to a string sentence. Print the result on the terminal. 
#   my_list = [ "The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]

my_list = ["the","quick","brown","fox","jumps","over","the","lazy","dog."]
joint_sentence = " ".join(my_list)
print(joint_sentence)


# Change the value of True in this list to False. Print the result on the terminal
# new_list = ['this', "brown", 55, "oxen", True, 0.85]

new_list = ["this","brown", 55, "oxen", "True", 0.85]
new_list[-2]=False
print(new_list)


#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements
# sample list ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color_list = ["Red","Green","White","Black","Pink","Yellow"]
primary_color = color_list[1:4]
print(primary_color)


# Write a program that takes in the user input of his favourite colour and adds it to an existing list of colours.
# color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
favorite_color = ['Blue']
final_list = color_list + favorite_color
print(final_list)
