####Written March 2013
##Time features added April 2013
##User dynamic added May 2015
from random import randint
import datetime, time, sys, easygui, pickle

timed = False
endnow = False
done = False
kill = False
tooktest = False
inuse = False
alreadyin = False

current_user = None

#Final result variables#
test_num = 0
rght_num = 0
wrng_num = 0
ques_num = 0
user_num = 2

user_id = {}
signin_data = {}
user_itls = []

savepath = ""

quikopen = open(savepath+'usermaps.pkl', 'r')
userinfolist = pickle.load(quikopen)
quikopen.close()
user_id = userinfolist[0]
signin_data = userinfolist[1]
user_num = userinfolist[2]
user_itls = userinfolist[3]

####Class User defines the parameters of a program user
class User():
    def __init__(self, username, realname, password, dob):
        self.username = username
        self.realname = realname
        self.password = password
        self.dob = dob
        self.test_num = 0
        self.id = None
        self.itl = False

    def testover(self):
        self.test_num += 1

    def identify(self):
        global user_num
        self.id = user_num + 1
        user_num += 1

    def infodump(self):
        df = open(savepath+'users/%s.txt' % self.id, 'w')
        df.write('User Info - ID %s\nName: %s %s\nUsername: %s\nPassword: %s\nDate of Birth: %s/%s/%s\n# Tests Taken: %s' % (self.id, 
                        self.realname[0], self.realname[1], 
                        self.username, self.password, self.dob[0], 
                        self.dob[1], self.dob[2], self.test_num))

def namestripper(orig):
    bob = orig.strip()
    joe = bob.strip('.')
    jack = joe.lower()
    return jack

def choices(msg, title, choice):
    abc = easygui.buttonbox(msg=msg, title=title, choices=choice)
    return abc

def admin_mode(msg, title):
    global guiset
    global done
    global endnow
    global kill
    admindone = False
    while not admindone:
        a = easygui.buttonbox(msg=msg, title=title, choices=['Users', 'Options', 'Exit'])
        if a == 'Options':
            dfile = open(savepath+"guiset.pkl", 'r')
            guiset = pickle.load(dfile)
            dfile.close()
            if guiset == True:
                currentguiset = 'on'
            elif guiset == False:
                currentguiset = 'off'
            a1 = choices('Please choose mode. EasyGui is currently %s.' %currentguiset, 'Mode', ['EasyGui ON', 'EasyGui OFF'])
            if a1 == 'EasyGui ON':
                guiset = True
            elif a1 == 'EasyGui OFF':
                guiset = False
            savegui = easygui.boolbox('Save EasyGui settings?', 'EasyGui Save')
            if savegui == 1:
                sfile = open(savepath+"guiset.pkl", 'w')
                pickle.dump(guiset, sfile)
                sfile.close()
            elif savegui == 0:
                pass
        elif a == 'Users':
            a1 = choices('Pick an option', 'User Menu', ['View Users', 'Create a User'])
            if a1 == 'View Users':
                password2 = easygui.passwordbox('Enter your admin password.', 'Password entry')
                if password2 == '171644':
                    userinfo1 = []
                    userinfo = ''
                    for i in range(user_num):
                        userfile = open(savepath+"users/%s.txt" % str(i+1), 'r')
                        userinfo1 = userinfo1 + userfile.readlines()
                        userinfo = userinfo + userinfo1[i+1]
                        userfile.close()
                    easygui.textbox('Here is information for all users.', 'User Info', userinfo)
                else:
                    easygui.msgbox('Your access to sensitive info has been denied.', 'ACCESS DENIED')
        elif a == 'Exit':
            exitchoice = choices('Choose your exit method', 'CHOOSE', ['Exit Admin', 'Exit Program', 'Back'])
            if exitchoice == 'Exit Admin':
                admindone = True
            elif exitchoice == 'Exit Program':
                admindone = True
                done = True
                endnow = True
                kill = True
            elif exitchoice == 'Back':
                pass

tsv = input("Math test program. Press Enter. ")
if tsv == "rothli":
    print("You have access, admin!")
    admin_mode("Welcome, administrator!", "Admin Menu")

elif tsv == "exit":
    done = True
    endnow = True
    kill = True

if endnow == False:
    dfile = open(savepath+"guiset.pkl", 'r')
    guiset = pickle.load(dfile)
    dfile.close()

    bgng = datetime.datetime.now()
    try:
        pklfil1 = open(savepath+"time.pkl", 'w')
        pickle.dump(bgng, pklfil1)
        pklfil1.close()
    except:
        pass

    try:
        pklfil2 = open(savepath+"time.pkl", 'r')
        lasttime = pickle.load(pklfil2)
        if guiset == False:
            print("The last time this program was run was ", lasttime)
        elif guiset == True:
            easygui.msgbox('The last time this program was run was %s' % str(lasttime), 'Time')
    except:
        pass

    if guiset == False:
        isuser = input('\nAre you a user? (Y/N) ')
        if isuser.lower().startswith('y'):
            MadAxeMan = input('Would you like to use EasyGui temporarily for more security? (Y/N) ')
            if MadAxeMan.lower().startswith('y'):
                passwordA = easygui.multpasswordbox('Enter your login info', 'User Login', ["Username", "Password"])
                username = namestripper(passwordA[0])
                password = passwordA[1]
            else:
                username = namestripper(input('Enter your username: '))
                password = input('Enter your passsword: ')
        else:
            print("That's too bad, but you can continue anyway.")
    elif guiset == True:
        isuser1 = easygui.boolbox('Are you a user?', 'User???')
        if isuser1 == 1:
            isuser = 'y'
        else:
            isuser = 'Happy valley was no longer happy.'
        if isuser.lower().startswith('y'):
            fieldVals = ['Username', 'Password']
            passwordA = easygui.multpasswordbox('Enter your login info', 'User Login', fieldVals)
            while 1:
                errmsg = ''
                if passwordA == None:  break
                for i in range(len(passwordA)):
                    if i >= 1:
                        argh = '\n'
                    else:
                        argh = ''
                    if passwordA[i] == '':
                        errmsg = errmsg + '%sPlease enter your %s' % (argh, fieldVals[i])
                if errmsg == '':  break
                passwordA = easygui.multpasswordbox(errmsg, 'User Login', fieldVals)
            if passwordA != None:
                username = namestripper(passwordA[0])
                password = passwordA[1]
            else:
                easygui.msgbox('Erm... Okay, then.', 'Eh?')
        else:
            bemuser = easygui.boolbox('Would you like to become a user?', 'New User')
            if bemuser == 1:
                easygui.msgbox("Okay, let's begin your application!", "Applying Time")
                namepass = easygui.multenterbox('Enter what you would like each to be.', 'Application', ['Username', 'Password', 'Reenter Password'])
                while 1:
                    errmsg = ''
                    if namepass[1] != namepass[2]: toejam = True
                    else:  toejam = False
                    if namepass[1] == '' and namepass[0] == '': finfish = True
                    else: finfish = False
                    if namepass[0] == '' or namepass[0] == None: nosweat = True
                    else:  nosweat = False
                    if toejam == False and nosweat == False and finfish == False: break
                    elif toejam == True: errmsg = "Please try again. The password fields don't match."
                    elif finfish == True and nosweat == False: errmsg = "You left the password fields blank."
                    elif nosweat == True and finfish == False: errmsg = "You left the username field blank."
                    elif nosweat == True and finfish == True: errmsg = "You left all of the fields blank."
                    for i in range(len(user_id)+1):
                        #print 'I iterated once.'
                        if namepass[0] == user_id[i + 1]:
                            errmsg = errmsg + '\nInvalid username.'
                            break
                    if errmsg == '': break
                    else:
                        namepass = easygui.multenterbox(errmsg, 'Application', ['Username', 'Password', 'Reenter Password'])
                namenames = ['First Name', 'Last Name']
                nametime = easygui.multenterbox('Please enter your name', 'Application', namenames)
                while 1:
                    errmsg = ''
                    if nametime == None:  break
                    for i in range(len(nametime)):
                        if i >= 1:
                            argh = '\n'
                        else:
                            argh = ''
                        if nametime[i] == '':
                            errmsg = errmsg + '%sPlease enter your %s' % (argh, namenames[i])
                    if errmsg == '':  break
                    nametime = easygui.multpasswordbox(errmsg, 'Application', namenames)
                datenames = ['Month', 'Day', 'Year']
                birthdate = easygui.multenterbox('Please enter your birthdate.', 'Application', datenames)
                while 1:
                    errmsg = ''
                    if birthdate == None:  break
                    for i in range(len(birthdate)):
                        if i >= 1:
                            argh = '\n'
                        else:
                            argh = ''
                        if birthdate[i] == '':
                            errmsg = errmsg + '%sPlease enter the %s' % (argh, datenames[i])
                    if errmsg == '':  break
                    birthdate = easygui.multpasswordbox(errmsg, 'Application', datenames)

                current_user = User(namestripper(namepass[0]), nametime, namepass[1], birthdate)
                current_user.identify()
                current_user.initial()
                user_id[current_user.id] = current_user.username
                signin_data[current_user.username] = current_user.password
                user_file = open(savepath+'users/%s.pkl' % current_user.username, 'w')
                pickle.dump(current_user, user_file)
                user_file.close()
                username = current_user.username
                password = current_user.password
                alreadyin = True
                inuse = True
                easygui.msgbox('Your application was a success!', 'Application', 'Yay!')
            elif bemuser == 0:
                alreadyin = True

    login = False
    if alreadyin != True:
        for i in range(len(user_id)+1):
            #print 'I iterated once.'
            if username == user_id[i + 1]:
                login = True
                break

    if login == True:
        if password == signin_data[username]:
            user_file = open(savepath+'users/%s.pkl' % username, 'r')
            current_user = pickle.load(user_file)
            user_file.close()
            inuse = True
            if guiset == True:
                easygui.msgbox('You are now signed in, %s!' % current_user.realname[0], 'Good Job')
            else:
                print('You are now signed in, %s!' % current_user.realname[0])
        else:
            print('No Credential Match')
    else:
        pass #print 'login ERROR'


####Single test loop:
def test():
    global done
    global tooktest
    global test_num
    global wrng_num
    global rght_num
    global ques_num
    while not done:
        print("--------------------------------------------------------------------------------")

        if guiset == True:
            easygui.msgbox('Your math test will now begin.', 'Math Test')

        #Test result variables#
        wrng = []
        right = 0
        no = 1

        print("")
        test_num += 1

        if guiset == False:
            t = input("Would you like to be timed (Y/N)? \n")
            if t.lower().startswith("y"):
                timed = True
            else:
                timed = False
            print("Would you like 1. addition, 2. subtraction, 3. multiplication, 4. division, or 5. all four?") 
            typ = input()
            ques = int(input("How many questions do you want? "))
        elif guiset == True:
            if choices('Would you like to be timed?', 'Timer', ['Yes', 'No']) == 'Yes':
                timed = True
            else: timed = False
            atyp = easygui.choicebox(msg='Please choose your test type', title='Test Type', 
                                    choices=['Addition', 'Subtraction', 'Multiplication', 'Division', 'All 4'])
            if atyp == 'Addition':
                typ = '1'
            elif atyp == 'Subtraction':
                typ = '2'
            elif atyp == 'Multiplication':
                typ = '3'
            elif atyp == 'Division':
                typ = '4'
            elif atyp == 'All 4':
                typ = '5'
            ques = int(easygui.enterbox(msg='How many problems do you want?', title='Problems'))
        print("")
        #Countdown to start test#
        time.sleep(1)
        print("Starting...")

        for i in range (5,0,-1):
            print(i)
            time.sleep(1)

        print("Now! \n")
        start = datetime.datetime.now()

        ####Problem loop:
        for index in range(ques):  #Loops the number of times entered before#
            if typ == "3":
                us = "x"   #Variable "us" tells the computer what symbol to show#

                y=randint(0,10)
                x=randint(0,10)

                cs = y*x  #Variable "cs" tells the computer what the problem is#

            if typ == "1":
                us = "+"

                y=randint(0,10)
                x=randint(0,10)

                cs = y+x

            if typ == "2":
                us = "-"

                y=randint(0,20)
                x=randint(0,y)  #Makes sure the answer is never a negative number#

                cs = y-x

            if typ == "4":
                us = "/"

                z=randint(0,10)
                x=randint(1,10)
                y=z*x   #Guarantees that answer is a whole number#

                cs = y/x

            if typ == "5":
                ty2 = randint(1,4)
                if ty2 == 1:
                    us = "+"

                    y=randint(0,10)
                    x=randint(0,10)

                    cs = y+x

                if ty2 == 2:
                    us = "-"

                    y=randint(0,20)
                    x=randint(0,y)

                    cs = y-x

                if ty2 == 3:
                    us = "x"

                    y=randint(0,10)
                    x=randint(0,10)

                    cs = y*x

                if ty2 == 4:
                    us = "/"

                    z=randint(0,10)
                    x=randint(1,10)
                    y=z*x

                    cs = y/x


            ##Problem results print here##
            print(no,". ",y,us,x,"=")       #Prints problem number and problem#
            ans = input("Enter your answer. ")
            print("You entered %s." %ans)
            try:
                if int(ans)==cs:
                    print("Correct! \n")
                    right += 1  #Adds 1 to score if answer correct#
                    rght_num += 1

                if int(ans)!=cs:
                    print("Incorrect.")
                    print("The correct answer is %s. \n" %cs) #Prints correct answer if incorrect#
                    wrng.append(no)
                    wrng_num += 1
                no += 1
            except:
                print("Incorrect.")
                print("The correct answer is %s. \n" %cs)
                wrng.append(no)
                wrng_num += 1
                no += 1
        end = datetime.datetime.now()

        ##Timed block##
        if timed:
            diff = end - start
            test_time = diff.seconds + diff.microseconds / float(1000000)
            ppw = (ques / test_time) * 60

            print("You finished", ques, "problems in %.1f seconds, or %.1f problems per minute. \n" %(test_time, ppw))

        print("You got",right,"out of",ques,"questions correct.") 
        if len(wrng) > 0: #Modifies list to show results with correct grammar#
            if len(wrng) == 1:
                w = str(wrng)
                r = w.replace("[","")
                wrong = r.replace("]","")
                prblm = "Problem"
                z = "was"
            if len(wrng) == 2:
                w = str(wrng)
                r = w.replace("[","")
                n = r.replace("]","")
                wrong = n.replace(","," and")
                prblm = "Problems"
                z = "were"
            if len(wrng) > 2:
                g = wrng.pop()
                w = str(wrng)
                r = w.replace("[","")
                n = r.replace("]","")
                wrong = n + ", and " + str(g)
                prblm = "Problems"
                z = "were"
            print("%s %s %s wrong." % (prblm, wrong, z))
        percent = float((float(right)/float(ques))*100) #Calculates percent correct#
        prcnt = float(percent)
        print("That is %.2f percent correct."%prcnt) #Tells percent correct#

        ques_num += ques

        if guiset == False:
            print("Would you like to file your results (Y/N)? ")
            fl = input()
        elif guiset == True:
            spongebob = easygui.boolbox('Would you like to file your results?', 'Filing')
            fl = 'n'

        ####Filer system in this block:
        if fl.lower().startswith('y') or spongebob == 1:
            try:
                a = open("Math Scores.txt", 'a')
                if guiset == False:
                    name = input("Enter your name or S to remain anonymous. ")
                elif guiset == True:
                    name = easygui.enterbox('Enter your name or S to remain anonymous.', 'Name')
                if name.lower() == 's':
                    name = "N/A"

                if typ == "1":
                    b = "Addition"
                if typ == "2":
                    b = "Subtraction"
                if typ == "3":
                    b = "Multiplication"
                if typ == "4":
                    b = "Division"
                if typ == "5":
                    b = "All four"

                a.write("\n")
                a.write("Name: %s" % name)
                a.write("\n")
                a.write(str(bgng))
                a.write("\n")
                a.write(b)
                a.write("\n")
                a.write("%i problems taken" % ques)
                a.write("\n")
                a.write("%i problems correct" % right)
                a.write("\n")
                a.write("%.2f percent correct" % prcnt)
                if timed:
                    a.write("\n")
                    a.write("Test completeted in %.1f seconds" % test_time)
                    a.write("\n")
                    a.write("%.1f problems per minute" % ppw)
                a.write("\n")
                a.close()
                print("Results Filed")
            except: #If error, do something else#
                print("FileError, results could not be filed.")
                try:
                    a.write("\n")
                    a.write("FileError")
                    a.write("\n")
                    a.close()
                except:
                    print("File could not be opened.")
        tooktest = True
        if inuse == True:
            current_user.testover()
        print("")
        if guiset == False:
            print("Would you like to take another test (Y/N)?")
            new_test = input()
            if new_test.lower().startswith("n"):
                done = True
            else:
                done = False
        elif guiset == True:
            new_test = easygui.boolbox('Would you like to take another test?', 'Testing')
            if new_test == 1:
                done = False
            else: done = True


####Final results print in this block:

#test()

if kill == False and endnow == False:
    if guiset == False:
        ghjkl = input('Would you like to take a test? (Y/N)')
        if ghjkl.lower().startswith('y'):
            ww23 = input('Take a 1. Math Test, or a 2. Typing test?')
            if ww23 == '1':
                test()
            else:
                pass
        else:
            pass

    elif guiset == True:
        LemJukes = easygui.ynbox('Would you like to take a test?', 'Test?')
        if LemJukes == 1:
            PETRA = easygui.buttonbox('Which kind of test do you want?', 'Big Decision, Man', ('Math Test', 'Typing Test'))
            if PETRA == 'Math Test':
                test()
            else:
                pass
        else:
            pass
elif kill == True:
    done = True
    endnow = True


quiksave = open(savepath+'usermaps.pkl', 'w')
pickle.dump([user_id, signin_data, user_num, user_itls], quiksave)
quiksave.close()

if inuse == True:
    user_file = open(savepath+'users/%s.pkl', 'w')
    pickle.dump(current_user, user_file)
    user_file.close()
    current_user.infodump()

print("")

if test_num == 1:   #All of this modifies for grammar#
    ttyp = "test"
else:
    ttyp = "tests"


if ques_num == 1:
    qtyp = "problem"
else:
    qtyp = "problems"


if rght_num == 1:
    rtyp = "problem"
else:
    rtyp = "problems"


if wrng_num == 1:
    wtyp = "problem"
else:
    wtyp = "problems"#All the way down to here!#

if endnow == False and tooktest == True:

    percent_2 = float(float(rght_num)/float(ques_num) * 100)

    print("You took %s %s." % (test_num, ttyp))  #This block shows FINAL results#
    print("And you took %s %s in all." % (ques_num, qtyp))
    print("You got %s %s right and %s %s wrong." % (rght_num, rtyp, wrng_num, wtyp))
    print("Or, %.2f percent correct." % percent_2)
    print("\nDone")
    d = input("Type OK to end.  ")
    while True:
        if d.lower() == 'ok':
            try:
                sys.exit()
            except:
                break
        break
if endnow == True:
    try:
        sys.exit()
    except:
        pass
