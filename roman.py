# http://codingdojo.org/kata/RomanCalculator/

from collections import OrderedDict

class Roman:
#        valid_symbol = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

    valid_symbol = OrderedDict()
    valid_symbol["I"] = 1
    valid_symbol["V"] = 5
    valid_symbol["X"] = 10
    valid_symbol["L"] = 50
    valid_symbol["C"] = 100
    valid_symbol["D"] = 500
    valid_symbol["M"] = 1000

    def __init__(self, value):
        """
        Can construct Roman number from string(with I,V,X,L,C,D and M inside) or with "classic" number
        """
        if type(value) is str:
            self.roman = value
            self.numeric = self.roman_to_numeric(value)
        elif type(value) is int:
            self.numeric = value
            self.roman = self.numeric_to_roman(value)

    def __str__(self):
        return "(" + self.roman + "," + str(self.numeric) + ")"

    def __eq__(self,other): 
        assert type(other) is Roman
        return self.numeric == other.numeric
    def __lt__(self,other):
        assert type(other) is Roman
        return self.numeric < other.numeric
    def __le__(self,other):
        assert type(other) is Roman
        return self.numeric <= other.numeric
    def __ne__(self,other):
        assert type(other) is Roman
        return self.numeric != other.numeric
    def __gt__(self,other):
        assert type(other) is Roman
        return self.numeric > other.numeric
    def __ge__(self,other):
        assert type(other) is Roman
        return self.numeric >= other.numeric

    def __add__(self,other):
        assert type(other) is Roman
        val_add = self.numeric + other.numeric
        return Roman(val_add)

    def __sub__(self,other):
        assert type(other) is Roman
        assert self.numeric > other.numeric
        val_add = self.numeric - other.numeric
        return Roman(val_add)

    def __mul__(self,other):
        if type(other) is Roman:
            val_add = self.numeric * other.numeric
        elif type(other) is int:
            val_add = self.numeric * other
        return Roman(val_add)

    def __rmul__(self, other):
        if type(other) is Roman:
            val_add = self.numeric * other.numeric
        elif type(other) is int:
            val_add = self.numeric * other
        return Roman(val_add)

    def validate_value(self,value):
        """
        Validate if a string is a valid roman number:
        Can only contains valid symbol(I,V,X,L,C,D,M)
        Can not contain more than 3 I or X or C in a row or more than 1 V or L or D in a row
        """
        for i,elem in enumerate(value):
            if elem not in Roman.valid_symbol.keys():
                raise ValueError("Not a valid roman number, contain invalid symbol")
            if elem in ["I","X","C"]:
                if i >= len(value)-3:
                    continue
                elif elem == value[i+1] and elem == value[i+2] and elem == value[i+3]:
                    raise ValueError("Not a valid roman number, contain more than three time the symbol '" + elem +"' consecutively")
            if elem in ["V","L","D"]:
                if i == len(value)-1:
                    continue
                elif elem == value[i+1]:
                    raise ValueError("Not a valid roman number, contain more than one time the symbol '" + elem +"' consecutively")

    def roman_to_numeric(self,value):
        self.validate_value(value)
        num = 0
        temp_val = 0
        for i, c in enumerate(value):
            if i == len(value)-1:
                num+=Roman.valid_symbol[c]
            elif value[i+1] == c:
                temp_val+=Roman.valid_symbol[c]
            elif Roman.valid_symbol[value[i+1]]>Roman.valid_symbol[c]:
                temp_val += Roman.valid_symbol[c]
                num-=temp_val
                temp_val = 0
            else:
                num+=temp_val
                num+=Roman.valid_symbol[c]
                temp_val = 0
        num+=temp_val
        return num

    def compute_roman(self,value,symbol):
        roman = ""
        v_symbol = Roman.valid_symbol[symbol]
        val = value
        if val >= v_symbol:
            val-= v_symbol
            roman+= symbol
            while val>= v_symbol:
                val-= v_symbol
                roman+= symbol
        if symbol in ["M","C","X"] and val >= 9*Roman.valid_symbol[symbol]/10:
            l = list(Roman.valid_symbol.keys())
            i = l.index(symbol)
            before = l[i-2]
            roman+= before
            roman+= symbol
            val -= 9*Roman.valid_symbol[before]
        if symbol in ["D","L","V"] and val >= 4*Roman.valid_symbol[symbol]/5:
            l = list(Roman.valid_symbol.keys())
            i = l.index(symbol)
            before = l[i-1]
            roman+= before
            roman+= symbol
            val -= 4*Roman.valid_symbol[before]
        return roman,val

    def numeric_to_roman(self,value):
        r = ""
        val = value
        for elem in reversed(Roman.valid_symbol.keys()):
            roman,val = self.compute_roman(val,elem)
            r+= roman
        return r

#if __name__ == "__main__":

