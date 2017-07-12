from ops import *

print "###########################################################\n"
print "#####################CALCULATOR############################\n"
print "###########################################################\n"
print "\t\t\t"
print "1. simple calc\n"
print "2. Sci calc\n"
print "3. exit\n\n"
calcOption = input("Please input an option :")

a = 1

if calcOption == 1:
    simpleCalcObj = simpleCalc()
    print "\nSimple calc\n"
    print "---------------\n\n"
    print "1. Add\n"
    print "2. Sub\n"
    print "3. Mul\n"
    print "4. Div\n"
    print "5. go back\n"
    simpleOption = input("Please specify a simple calc operation: ")
    if simpleOption == 1:
        print "\nAdd Operation: \n"
        addVar1 = input("Please input the 1st value: ")
        addVar2 = input("Please input the 2nd value: ")
        result = simpleCalcObj.add(addVar1,addVar2)
        print result
        
    
        