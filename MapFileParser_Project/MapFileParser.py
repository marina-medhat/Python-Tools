import sys
import re

"""Baby Names exercise

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h1>Popular Names by Birth Year</h1>September 12, 2007</td>
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...
"""



def MapFun():
  # +++your code here+++
  for j in sys.argv[1:]:
    sumText=0
    sumBss=0
    sumRoData=0
    sumData=0
    f=open('Project_Memory_Map_File.map','r')
    f1=open(j+'_INFO','w')
    f.seek(0)
    s=f.read()
    match=re.findall(r'\w+\W(\w+)\s+\Wtext\s+'+j+'\w+\W\w',s)
    for i in match :
      sizText=int(i,16)
      sumText=sumText+sizText
      
    match=re.findall(r'\w+\W(\w+)\s+\Wbss\s+'+j+'\w+\W\w',s)
    for i in match :
      sizbss=int(i,16)
      sumBss=sumBss+sizbss
      
    match=re.findall(r'\w+\W(\w+)\s+\Wrodata\s+'+j+'\w+\W\w',s)
    for i in match :
      sizro=int(i,16)
      sumRoData=sumRoData+sizro
      
    match=re.findall(r'\w+\W(\w+)\s+\Wdata\s+'+j+'\w+\W\w',s)
    for i in match :
      sizdata=int(i,16)
      sumData=sumData+sizdata
    
    f1.write('            ***** '+j+' component Info *****\n\n')  
    f1.write('Size of .text   section in '+j+' component is ='+str(sumText)+'Bytes\n') 
    f1.write('Size of .rodata section in '+j+' component is ='+str(sumRoData)+'Bytes\n\n')  
    f1.write('Size of .data   section in '+j+' component is = '+str(sumData)+'Bytes\n')  
    f1.write('Size of .bss    section in '+j+' component is ='+str(sumBss)+'Bytes\n\n')  
    f1.write('-> Size of ROM in '+j+' component is ='+str(sumText+sumRoData)+'Bytes\n')  
    f1.write('-> Size of RAM in '+j+' component is ='+str(sumBss+sumData)+'Bytes\n')   
            

    
def main():
  MapFun()
  
'''
There is something missing Here :)
'''
if __name__ == '__main__':
  main()
  