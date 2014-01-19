import math

att_level = float(raw_input("What is your Attack level?"))
str_level = float(raw_input("What is your Strength level?"))
def_level = float(raw_input("What is your Defence level?"))
hit_level = float(raw_input("What is your Hitpoint level?"))
range_level = float(raw_input("What is your Range level?"))
pray_level = float(raw_input("What is your Prayer level?"))
mage_level = float(raw_input("What is your Magic level?"))

base_cmb = (0.25*(def_level+hit_level+(math.floor(pray_level/2))))
melee_cmb = (0.325*(att_level+str_level))
mage_cmb = (0.325*((math.floor(mage_level/2)+mage_level)))
range_cmb = (0.325*((math.floor(range_level/2)+range_level)))

if mage_level > range_level:
    if (mage_level*1.5) > (att_level+str_level):
        print "Your combat level is Magic based!\n Your combat level is:"
        magic = (base_cmb+mage_cmb)
        print magic
    else:
        print "Your combat level is Melee based!\n Your combat level is:"
        melee = (base_cmb+melee_cmb)
        print melee
        
if range_level > mage_level:
    if (range_level*1.5) > (att_level+str_level):
        print "Your combat level is Range based!\n Your combat level is:"
        rang = (base_cmb+range_cmb)
        print rang
    else:
        print "Your combat level is Melee based!\n Your combat level is:"
        melee = (base_cmb+melee_cmb)
        print melee
        
if range_level == mage_level:
    equal_levels = range_level*1.5
    if equal_levels > att_level+str_level:
        print "Your combat level is Range/Magic based!\n Your combat level is:"
        rangmage = (base_cmb+range_cmb)
        print rangmage
    else:
        print "Your combat level is Melee based!\n Your combat level is:"
        melee = (base_cmb+melee_cmb)
        print melee
            
    
