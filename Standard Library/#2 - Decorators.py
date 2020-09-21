from datetime import datetime as dt
import functools
#==================================================
#INTRODUCTION

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper #A decorator must return the memory address
                   #of the function that will be applied

@my_decorator #This is equivalent to say_whee = my_decorator(say_whee)
def say_whee():
    print("Whee!")

#===================================================
#SHORT EXAMPLE
    
def mult_2(func):
    def internal():
        return func()*2
    return internal

@mult_2
def dois():
    return 2
#=================================================
#A FUNCTION WHICH ACTIVATES ONLY AT DAY

def not_during_the_night(func):
    def wrapper():
        if 7 <= dt.now().hour < 22: #I have to learn datetime
            func()
        else:
            pass
    return wrapper

@not_during_the_night #If we use the decorator, this function will not
                      #work during the night
def scream():
    print("AAAAAAHHH!!")

#===================================================
# A DECORATOR WHICH DOES EVERYTHING TWICE
def twice(func):
    def internal():
        func()
        func()
    return internal

@twice #Same as scream_2 = twice(scream_2)
def scream_2():
    print("UUUUUUUHHHH")
    
#============================================
# IF WE WANTED TO WRAP A FUNCTION WITH PARAMETERS,
# WE HAVE TO USE ARGS AND KWARGS

def do_twice(func):
    @functools.wraps(func) #Necessary to function auto-recognition
    def internal(*args, **kwargs):
        func(*args,**kwargs)
        return func(*args,**kwargs) #Remember to return if you want to use
                                     #it's value after
    return internal

@do_twice
def say(word):
    print(f"I love to say {word}")
#==========================================
#Stopped at 'timing functions'
