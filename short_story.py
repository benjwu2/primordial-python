## There once was a ____ _____ named ____. ____ had 3 ____s. The end

adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
name = input("Enter a name: ")
noun2 = input("Enter a noun: ")

def shortStory(adjective, noun, name, noun2):
    sentence1 = "There once was a {} {} named {}. ".format(adjective, noun, name)
    sentence2 = "{} had 3 {}s. The end.".format(name, noun2)
    print(sentence1 + sentence2)
    return

shortStory(adjective, noun, name, noun2)