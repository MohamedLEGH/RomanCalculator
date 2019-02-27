from roman import Roman

def test_numeric():
    assert 1 == Roman("I").numeric
    assert 2 == Roman("II").numeric
    assert 3 == Roman("III").numeric
    assert 4 == Roman("IV").numeric
    assert 5 == Roman("V").numeric
    assert 6 == Roman("VI").numeric
    assert 7 == Roman("VII").numeric
    assert 8 == Roman("VIII").numeric
    assert 9 == Roman("IX").numeric
    assert 10 == Roman("X").numeric
    assert 11 == Roman("XI").numeric
    assert 12 == Roman("XII").numeric
    assert 13 == Roman("XIII").numeric
    assert 14 == Roman("XIV").numeric
    assert 15 == Roman("XV").numeric
    assert 16 == Roman("XVI").numeric
    assert 17 == Roman("XVII").numeric
    assert 18 == Roman("XVIII").numeric
    assert 19 == Roman("XIX").numeric
    assert 20 == Roman("XX").numeric
    assert 30 == Roman("XXX").numeric
    assert 40 == Roman("XL").numeric
    assert 50 == Roman("L").numeric
    assert 60 == Roman("LX").numeric
    assert 70 == Roman("LXX").numeric
    assert 80 == Roman("LXXX").numeric
    assert 90 == Roman("XC").numeric
    assert 100 == Roman("C").numeric
    assert 101 == Roman("CI").numeric
    assert 105 == Roman("CV").numeric
    assert 110 == Roman("CX").numeric
    assert 150 == Roman("CL").numeric
    assert 200 == Roman("CC").numeric
    assert 300 == Roman("CCC").numeric
    assert 400 == Roman("CD").numeric
    assert 500 == Roman("D").numeric
    assert 600 == Roman("DC").numeric
    assert 700 == Roman("DCC").numeric
    assert 800 == Roman("DCCC").numeric
    assert 900 == Roman("CM").numeric
    assert 1000 == Roman("M").numeric
    assert 2000 == Roman("MM").numeric
    assert 2019 == Roman("MMXIX").numeric

def test_roman():
    assert Roman(1).roman == "I"
    assert Roman(2).roman == "II"
    assert Roman(3).roman == "III"
    assert Roman(4).roman == "IV"
    assert Roman(5).roman == "V"
    assert Roman(6).roman == "VI"
    assert Roman(7).roman == "VII"
    assert Roman(8).roman == "VIII"
    assert Roman(9).roman == "IX"
    assert Roman(10).roman == "X"
    assert Roman(11).roman == "XI"
    assert Roman(12).roman == "XII"
    assert Roman(13).roman == "XIII"
    assert Roman(14).roman == "XIV"
    assert Roman(15).roman == "XV"
    assert Roman(16).roman == "XVI"
    assert Roman(17).roman == "XVII"
    assert Roman(18).roman == "XVIII"
    assert Roman(19).roman == "XIX"
    assert Roman(20).roman == "XX"
    assert Roman(30).roman == "XXX"
    assert Roman(40).roman == "XL"
    assert Roman(50).roman == "L"
    assert Roman(60).roman == "LX"
    assert Roman(70).roman == "LXX"
    assert Roman(80).roman == "LXXX"
    assert Roman(90).roman == "XC"
    assert Roman(100).roman == "C"
    assert Roman(101).roman == "CI"
    assert Roman(105).roman == "CV"
    assert Roman(110).roman == "CX"
    assert Roman(150).roman == "CL"
    assert Roman(200).roman == "CC"
    assert Roman(300).roman == "CCC"
    assert Roman(400).roman == "CD"
    assert Roman(500).roman == "D"
    assert Roman(600).roman == "DC"
    assert Roman(700).roman == "DCC"
    assert Roman(800).roman == "DCCC"
    assert Roman(900).roman == "CM"
    assert Roman(1000).roman == "M"
    assert Roman(2000).roman == "MM"
    assert Roman(2019).roman == "MMXIX"
    
def test_add():
    assert Roman("II") == Roman("I") + Roman("I")
    assert Roman("IV") == Roman("II") + Roman("II")
    assert Roman("V") == Roman("III") + Roman("II")
    assert Roman("V") == Roman("II") + Roman("III")
    assert Roman("M") == Roman("D") + Roman("D")

def test_add():
    assert Roman("I") == Roman("II") - Roman("I")
    assert Roman("II") == Roman("IV") - Roman("II")
    assert Roman("II") == Roman("V") - Roman("III")
    assert Roman("D") == Roman("M") - Roman("D")
    
def test_mult_int():
    assert Roman("I") == Roman("I") * 1
    assert Roman("IV") == Roman("II") * 2
    assert Roman("IV") == 2 * Roman("II")
    assert Roman("IX") == Roman("III") * 3
    
def test_mult():
    assert Roman("I") == Roman("I") * Roman("I")
    assert Roman("IV") == Roman("II") * Roman("II")
    assert Roman("IX") == Roman("III") * Roman("III")
