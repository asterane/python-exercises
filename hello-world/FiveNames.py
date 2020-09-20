#Written July 2012#
#replace_l function added May 2013#
def replace_l(object):
    global final
    strject = str(object)
    n = strject.replace("[", "")
    a = n.replace("]", "")
    final = a.replace("'", "")
    

print("Enter five names:")
#Retrives five names from user#
name1 = input("1-> ") 
name2 = input("2-> ")
name3 = input("3-> ")
name4 = input("4-> ")
name5 = input("5-> ")
names = [name1, name2, name3, name4, name5]

replace_l(names)
print("The names are: %s." % final)
names2 = sorted(names) #copies and sorts the original names#
replace_l(names2)
print("The names sorted alphabetically are: %s." % final)

print("The third name you entered was:", names[2])

replace = int(input("Please choose one name to replace(1-5). "))
replace2 = int(replace)
r = replace2 - 1
names3 = names[:] #copies the original list#
del names3[r] #deletes somthing in the new list# 
print("Enter the name you want in that spot.")
newName = input()
names3.insert(r, newName)

replace_l(names3)
print("The names are: %s." % final)


