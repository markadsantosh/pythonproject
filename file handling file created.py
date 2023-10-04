import os
try:
    os.mkdir('./users')
except:
    print('users folder is created')
firstname=input('enter your first name:')
lastname=input('enter your last name:')
email=input('enter your mail :')

file=open(firstname+lastname,'a')
file.write('firstname={} \n'.format(firstname))
file.write('lastname={} \n'.format(lastname))
