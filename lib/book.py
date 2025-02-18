#!/usr/bin/env python3

class Book:
    def __init__(self, title,page_count):
      self.title = title
      self.page_count = page_count

    @property
    def page_count(self):# COPY the current value of properties
         return self._page_count

    @page_count.setter
    def page_count(self, page_count):#check if the value being pass in okay
         if isinstance(page_count, int):# check
           self._page_count = page_count# where the value being passed in
         else:
           print("page_count must be an integer")
    def turn_page(self):
       print("Flipping the page...wow, you read fast!")








