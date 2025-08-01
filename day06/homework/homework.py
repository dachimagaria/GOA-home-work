#დავალება 1
num1 =input()
num2 =input()
print(num1>num2)
print(num1<num2)
print(num1==num2)

#დავალენბა 2
num_1 ="100"
num_2 ="2000"
num_3 ="468"
num_4 =150
num_5 =300
int1 = int(num_1)
int2 = int(num_2)
int3 = int(num_3)
ნამრავლი = int1 * int2 * int3 * num_4 * num_5
print(ნამრავლი)
print(4212000000000 / 5)


#დავალება 3
name_1 =input()
name_2 =input()
number_1 =4000
print(name_1 + name_2*4000)

#დავალება 4
 #logical operation--> and და or. and_ის დროს ყველაზე დიდი უპირატესობა აქვს მინიჭებული false  მაგალითად 
 #ტერმინალზე გაშვების დროს ეს აუცილებლად false იქნება
 #ხოლო or_ს როცა ვიყენებთ Trues არის დიდი უპირატესობა მინიჭებული და ტერმინალზე აუცილებლად True დაწერს

#დავალება 5 
#     (and)                        
#True and True -- True   აქ იმიტომ არის True  რადგან ორივე მხარეს True წერია და ამიტომ დიდი უპირატესობა True-ს ექნება მინიჭებული                            
#True and False --False   აქ False-ია რადგან როცა and-ის გამოყენების დროს უპირატესობა False აქვს მინიჭებული                   
#False and True --False   აქაც False-ია                    
#False and False -- False  აქ False-ია რადგან ორივე მხარეს False წერია                  
 #True or True -- True აქ True-ა რადგან or-ის გამოყენების დროს დიდი უპირატესობა True-ს აქვს მინიჭებული
#True or False -- True აქაც იგივეა რაც წინაზე დავწერე ↑
#False or True -- True აქაც True
#False or False -- False აქ False ია რადგან True არ წერი


#დავალება 6
print(True and False)#-->False
print(True and True)#-->True
print(True or False)#-->True
print(False or False)#-->False


#დავალება 7
name = "dachi magaria"
number = 1500000000000
number2 = 1.0000000000002
random = True and False
print(type(name))#<class 'str'>
print(type(number))#<class 'int'>
print(type(number2))#<class 'float'>
print(type(random))#<class 'bool'>

#დავალება 8
A =float(input("შეიყვანე float: "))
B =int(input("შეიყვანე integer: "))
C = input("შეიყვანე string: ")

print(A)
print(B)
print(C)
