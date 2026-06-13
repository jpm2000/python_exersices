saludo = "Hola"
nombre = "Juan"

print(saludo, nombre)

print("")

print(saludo)
print(nombre)

print("")

saludo_1 = "Hi"
saludo_2 = "Hello"
nombre_1 = "Juan"
nombre_2 = "Pablo"

print(saludo_1)
print(saludo_2)
print(nombre_1)
print(nombre_2)

print("")

"""

Here is a sample line of code that can be executed in Python:
print("Hello, World!")

You can just as easily store a string as a variable and then print it to stdout:
my_string = "Hello, World!"
print(my_string)

The above code will print Hello, World! on your screen. Try it yourself in the editor below!

Input Format
You do not need to read any input in this challenge.

Output Format
Print Hello, World! to stdout.

Sample Output 0
Hello, World!

"""

story = "Once upon a time, there was a {} who loved {}"
character = "Wizard"
interest = "Magic"

print(story.format(character, interest))

print("")

story_2 = "He used to go up and down the {} while thinking about his new {}"
context = "Mountain"
characteristic = "trick"

print(story_2.format(context, characteristic))

print("")

then_what = input("What happened next?: ")

print(then_what)

print("")

final_cut = "The wizard was so {} that he {}. And could not see his very good friend JP ever again. Now he is looking for him in Heaven."

emotion = input("What emotion did the wizard feel?: ")
action = input("What action did the wizard take?: ")

print(final_cut.format(emotion, action))
