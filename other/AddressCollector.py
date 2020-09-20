#Written May 2013#
import easygui
ans1 = easygui.multenterbox(msg='Enter your address', 
title='Address Collector', 
fields=['Name:', 'Street address:', 'City, ST:', 'Zip code:'], 
values=())

ZpCd = ans1.pop()
CtSt = ans1.pop()
StAd = ans1.pop()
MyNm = ans1.pop()

ans2 = '%s \n%s \n%s \n%s' % (MyNm, StAd, CtSt, ZpCd)

easygui.msgbox(msg=ans2, title='Stats')

filesave = easygui.buttonbox(msg='Would you like to file: \n%s' % ans2, title='File Results?', choices=['Yes', 'No'])

if filesave == 'Yes':
    a = open("Addresses.txt", 'a')
    a.write("\n%s" % ans2)
    a.close()
    
else:
    pass #Creates code stub, does nothing#
