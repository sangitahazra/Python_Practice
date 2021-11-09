import time, sys,re
indent =1 # How many spaces to indent.
indent1=14
indentIncreasing = True # Whether the indentation is increasing or not.
print('Hi !!!! Babe')
print('I wanna say something to you please tell me your name:-')
name=input()
if(name.lower()=='manas'):
 print('============================================================================================================================')
 print('============================================================================================================================\n')

 for indent in range(1,10): # The main program loop.
  if indent==1:
   print('**********','      ','***','       ',' ********** ','  **',' '*(indent1),'**','  ************* ','      ','***        ***')

  elif indent>1 and indent<9 and indent!=5:
   print('    **    ','      ','***','       ','**        **',' '*indent,'**',' '*indent1,'**',' '*indent,'**','    ','              ***        ***')
  elif indent==5:
   print('    **    ','      ','***','       ','**        **',' '*indent,'**',' '*indent1,'**',' '*indent,'************* ','      ','***        ***')
  elif indent==9:
   print('**********','      ','********** ',' ********** ',' '*10,'**','           ************* ','      ','**************','\n')

  indent = indent + 1
  indent1=indent1-2
 print('============================================================================================================================')
 print('============================================================================================================================')
else:
 print('Sorry '+name+' you are not my LOVE')
