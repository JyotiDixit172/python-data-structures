# every data structure that we are going to create is by using classes

class Cookie:
    # if the class has self keyword, it is a method that is part of a class
    #  def -> that a function is initialised, but use of self differentiates it from a fucntion.

    #  def __init__ (self, parameter): -> constructor
    def __init__ (self,color):
        #  if in the class you pass, green -> that green parameter gets passed -> self.color 
        # self.color is gonna apply to the specific instance of color we are passing
        self.color = color

# variable_name = class(argument)
#  this green gets passed to the constructor -> which creates a green cookie
cookie_one = Cookie("green")
#  constructor passes itself (self) a new cookie -> which is blue
cookie_two = Cookie("blue")

#  so that is how we are able to create a two different cookie's using a same class.

#  It's using same dough as constructor -> using self - > to use two different colors to bake green & purple cookie


# ALONG eith constructor we can use other methods to do other things with this cookie class.

# start tomorrow