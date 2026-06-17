name = "aishik"

print(len(name)) # returns the loength of the string

#To check the ending of the string
print(name.endswith("K"))
print(name.endswith("k"))
print(name.endswith("hik"))

#To check the starting of the string
print(name.startswith("hik"))
print(name.startswith("A"))
print(name.startswith("Ais"))

print(name.capitalize()) # Capitalizes the 1st the character of the string

# to search for a specific word
sen = """Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night. 

Then the traveller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so. 

In the dark blue sky you keep,
And often through my curtains peep,
For you never shut your eye,
Till the sun is in the sky. 

'Tis your bright and tiny spark,
Lights the traveller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star"""

print(sen.find("wonder")) # returns the the index of the 1st character of the word
print(sen.find("o")) # returns the index of the 1st instance of 'o' in the sentence

# To replace a word
replaced = sen.replace("little", "big") # replaces every instance of the word "little" with "big"
print(replaced)