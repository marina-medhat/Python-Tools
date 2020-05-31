import sys,os


def MakeDrive():
  print('Hello to Python Script Making Any Driver Folder')
  Dname=input('Enter Name Of Ur Driver:')
  os.mkdir('01-'+Dname)
  os.chdir('01-'+Dname)
  f=open(Dname+'_INTERFACE.h','w')
  f.close()
  f=open(Dname+'_CONFIG.h','w')
  f.close()
  f=open(Dname+'_PRIVATE.h','w')
  f.close()
  f=open(Dname+'_PROGRAM.c','w')
  f.close()
  f=open(Dname+'_REGISTERS.h','w')
  f.close()
  
  f=open(Dname+'_PROGRAM.c','r+')
  f.seek(0,2)
  f.write('#include "STD_TYPES.H"')
  f.write('\n')
  f.write('#include "BIT_MATH.h"')
  f.write('\n')
  f.write('#include "'+ Dname+'_INTERFACE.h"')
  f.write('\n')
  f.write('#include "'+ Dname+'_REGISTER.h"')
  f.write('\n')
  f.write('#include "'+ Dname+'_CONFIG.h"')
  f.write('\n')
  f.write('#include "'+ Dname+'_PRIVATE.h"')
  f.write('\n')
  f.close()
  
  











def main():
   MakeDrive()

if __name__ == '__main__':
  main()