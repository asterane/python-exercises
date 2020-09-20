#Written July 2012 
import easygui
easygui.msgbox("""Please continue if you would
like to play on the soccer team.""")
MoF = easygui.buttonbox("Select your gender.",
                        choices = ['M', 'F'] )
if MoF == 'F':
  Age = easygui.choicebox("Select your age",
                      choices = ['less than 4', '4-6', '6-8', '8-10', '10-12', 'more than 12'] )
  if Age == '10-12':
      easygui.enterbox("You can play on the team. Enter your name.")
      easygui.msgbox("The survey is over. Have a nice day.")
  else:
      easygui.msgbox("Sorry ,you cannot play on the team. Goodbye.")
else:
    easygui.msgbox("Sorry ,you cannot play on the team. Goodbye.")

