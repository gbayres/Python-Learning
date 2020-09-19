#First, we have to know about the parameter "key" in sorting function
#This parameter selects which elements the function should compare
#for instance, we can sort items by length:
names = ["Anna", "Lenna", "Victor", "Gabriel", "Tom"]
new_list = sorted(names, key=len)

#Out: ['Tom', 'Anna', 'Lenna', 'Victor', 'Gabriel']

#We can also sort by the second letter
new_list = sorted(names, key=lambda name: name[1])

#Out: ['Gabriel', 'Lenna', 'Victor', 'Anna', 'Tom']

#Remember:
def f(x):
    return x+2
#is the same as
f = lambda x: x+2

#So, if we have the following dict:
scores = {"Anna": 12,
          "Lenna": 54,
          "Victor": 32,
          "Gabriel": 17,
          "Tom": 33}

#We can sort items by value using:
new_list = sorted(scores.items(),
                  key = lambda item: item[1],
                  reverse = True)

#Out: [('Lenna', 54), ('Tom', 33), ('Victor', 32),
#      ('Gabriel', 17), ('Anna', 12)]

#Now we can have a list of the first places
positions = [item[0] for item in new_list]

#Out: ['Lenna', 'Tom', 'Victor', 'Gabriel', 'Anna']
