#!/usr/bin/env python

# encapsulation-1.py

# Encapsulation means to preserve data in classes using methods
# Here, we're setting the 'val' attribute through 'set_val()'.
# See the next example, `encapsulation-2.py` for more info

# In this example, we have two methods, `set_val` and `get_val`.
# The first one sets the `val` value while the second one
# prints/returns the value.


class MyClass(object):

    def set_val(self, val):
        self.value = val

    def get_val(self):
        print(self.value)
        return self.value

a = MyClass()
b = MyClass()

a.set_val(10)
b.set_val(100)

a.get_val()
b.get_val()
