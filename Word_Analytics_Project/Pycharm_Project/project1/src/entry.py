"""
Benjamin Mitchell
242-csapx
10/19/2016

Entry object used in the multiple dictionaries as the value
containing multiple pieces of varying data
"""
class Entry:

    __slots__ = 'strValue', 'number'

    def __init__(self, strValue, num):
        self.strValue = strValue
        self.number = num

    def getStrValue(self):
        return self.strValue
    def updateStrValue(self, num):
        self.strValue += num
    def getNumber(self):
        return self.number
    def updateNumber(self, num):
        self.number += num
