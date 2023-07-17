#!/usr/bin/python3
'''Class rectangle that inherits from the Base class'''

from models.base import Base


class Rectangle(Base):
    '''A recrangle class'''

    # class constructor
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''getter method for width'''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''seter method for  width'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''getter method for height'''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''seter method for  height'''
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''getter method for x'''
        return (self.__x)

    @x.setter
    def x(self, value):
        '''seter method for  x'''
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''getter method for y'''
        return (self.__y)

    @y.setter
    def y(self, value):
        '''seter method for y'''
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y  must be >= 0")
        self.__y = value

    def area(self):
        '''gives area of a rectangle'''
        return (self.width * self.height)

    def display(self):
        '''prints a rectange using the # character to stdout
        for i in range(self.__height):
            for j in range(self.__width):
                print('#',end='')
            print('')
        '''
        '''update to print Rectangle taking care of x and y'''
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        '''method that returns [Rectangle] (<id>) <x>/<y> - <width>/<height>'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        '''gives a dictionary representation of a Rectangle'''
        return ({
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x, "y": self.y})
