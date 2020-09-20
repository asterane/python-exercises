#Written July 2012
import easygui
b = "Programmer"
c = "Agent"
d = "Operative"

easygui.msgbox("Click OK.","Booting System...")
code = easygui.passwordbox("Enter the code.","Confirmation")
if code == "secret":
    Name = easygui.enterbox("Enter your first name.","Access Granted")
    if Name == 'Matthew':
        easygui.msgbox("Hello, programmer. You have acessed TOP SECRET information.",b)
        Mission = easygui.buttonbox("Do you choose to accept the mission?", "Accept",
                          choices = ['Yes', 'No'])
        if Mission == 'Yes':
            easygui.msgbox("Programming ROCKS!",b)
        elif Mission == 'No':
            easygui.msgbox("Goodbye, programmer.",b)
    elif Name == 'name2':
        easygui.msgbox("Hello, programmer. You have acessed TOP SECRET information.",b)
        Mission4 = easygui.buttonbox("Do you choose to accept the mission?", "Accept",
                                     choices = ['Yes', 'No'])
        if Mission4 == 'Yes':
            easygui.msgbox("---No info yet. Check back soon.---",b)
        elif Mission4 == 'No':
            easygui.msgbox("Goodbye, programmer.",b)
    else:
        easygui.msgbox("Welcome, agent. You have acessed SECRET information.",c)
        Mission2 = easygui.buttonbox("Do you choose to accept the mission?", "Accept",
                                     choices = ['Yes', 'No'] )
        if Mission2 == 'Yes':
            easygui.msgbox("---No info yet. Check back soon.---",c)
        elif Mission2 == 'No':
            easygui.msgbox("Goodbye, agent.",c)
elif code == 'conf':
    easygui.msgbox("Welcome, operative. You have acessed CONFIDENTIAL information.","Access Granted")
    Mission3 = easygui.buttonbox("Do you choose to accept the mission?", "Accept",
                                 choices = ['Yes', 'No'] )
    if Mission3 == 'Yes':
        easygui.msgbox("---No info yet. Check back soon.---",d)
    elif Mission3 == 'No':
        easygui.msgbox("Goodbye, operative.",d)
else:
    easygui.msgbox("That is the wrong code. Goodbye.", "ACCESS DENIED")
        
        
