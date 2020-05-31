import sys,os

def phoneBook():
  name=''
  number=0
  email=''
  
  if sys.argv[1] == 'add' :
    f2= open('Phones.txt','r+')
    f2.seek(0,2)
    
    
    name=input('Enter Name:')
    f2.write(name)
    f2.write('\t')
    
    number=input('Enter Phone:')
    f2.write(number)
    f2.write('\t')
    
    email=input('Enter Email:')
    f2.write(email)
    f2.write('\t')
    
    f2.write('\n')
    f2.close()
    
    
    
  elif sys.argv[1] == 'search' :
    name=input('Enter Name:')
    f2= open('Phones.txt','r')
    for line in f2 :
      words = line.split() 
      if words[0] == name:
        print('Name',words[0])
        print('Number',words[1])
        print('Email',words[2])
    f2.close()

  
  elif sys.argv[1] == 'printall' :
    c=1
    f2= open('Phones.txt','r')
    for line in f2 :
      words = line.split() 
      print('('+str(c)+')')
      print('Name',words[0])
      print('Number',words[1])
      print('Email',words[2])
      print('____________________')
      c+=1

    f2.close()
    
    f2.close()
  
  




def main():
   phoneBook()

if __name__ == '__main__':
  main()