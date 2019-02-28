[![Build Status](https://travis-ci.org/MohamedLEGH/RomanCalculator.svg?branch=master)](https://travis-ci.org/MohamedLEGH/RomanCalculator)
[![Coverage Status](https://coveralls.io/repos/github/MohamedLEGH/RomanCalculator/badge.svg?branch=master)](https://coveralls.io/github/MohamedLEGH/RomanCalculator?branch=master)

# RomanCalculator

based on code kata : http://codingdojo.org/kata/RomanCalculator/

## Install
```
(need python3)
pip install pytest pytest-cov
git clone https://github.com/MohamedLEGH/RomanCalculator
cd RomanCalculator
```

## Use
```
(in shell): python -i roman.py
>>> a = Roman("II")
>>> b = Roman(1)
>>> print(a)
(II,2)
>>> print(a.roman)
II
>>> print(a.numeric)
2
>>> print(a+a)
(IV,4)
>>>print(a-b)
(I,1)
>>> a == b
False
>>> a == Roman(2)
True
>>>print(3*a)
(VI,6)
```

## Test

```
py.test --cov=. .
```

