# Oliver Hugh 4/4/2022
from tkinter import *


class Table:
    def __init__(self, data: list, area: str):
        """
        Initiates a Table object, which will create a table in tkinter
        to display data
        :param data: the data that will be displayed in the table. Should be a list of lists
        :param area: where the table will be packed
        """
        self.data = data
        self.area = area

        #we will now iterate through the elements in data
        #to create a matrix of entries, which we will then display data in
        #go through rows
        for r in range(len(data)):
            for c in range(len(data[0])):
                self.box = Entry(master=area, width=5)
                self.box.grid(row=r, column=c)
                self.box.insert(END, data[r][c])




