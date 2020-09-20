import easygui
telling = easygui.enterbox("What would you like to tell me?",
                           default = 'I want to do a happy dance')
easygui.msgbox ("You told me " + telling)
