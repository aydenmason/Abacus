#AYDEN MASON
#9/6/2019
#CREATES A 13 ROW ABACUS.

#this fucntions job is to fill the abacus if there are unsed cols with empty cols.
def fill_abacus(abacus,strings):
  curr_size = len(abacus)
  for x in range(curr_size-1, 12):
    abacus.append(strings[str(0)])
  #reverse the abacus
  abacus.reverse()
  #this prints the list in columns instead of rows.
  for a,b,c,d,e,f,g,h,i,j,k,l,m in zip(*abacus):
    print(a,b,c,d,e,f,g,h,i,j,k,l,m)

#this fucntion builds and prints the abacus.
def build_col(sum):
  #dictionary of all the of ways a column can be drawn. 
  #this will be used to create each column
  strings = {
    '0':"oo  -    ooooo",
    '1':"oo  -o    oooo",
    '2': "oo  -oo    ooo",
    '3':"oo  -ooo    oo",
    '4' :"oo  -oooo    o",
    '5' :"o  o-    ooooo",
    '6' : "o  o-o    oooo",
    '7':"o  o-oo    ooo",
    '8':"o  o-ooo    oo",
    '9' :"o  o-oooo    o"
  }
  #create an object abacus, and make it a list data structure. 
  abacus = list()
  #this goes thru the sum,
  while(sum >0):
    #look at the most rigth hand digit and store it in digit
    digit = sum % 10
    #after looking at digit, slice it off
    sum = sum//10
    #debugging purposes.
    print(digit)
    #this adds an string to abacus depending on the digit that was sliced off.
    abacus.append(strings[str(digit)])
    #debugging
  for x in abacus:
    print(x)
  print(len(abacus))
  fill_abacus(abacus,strings)
#add two nums together from input 
first = int(input("first num = "))
second = int(input("second num = "))
sum = first+second
build_col(sum)
