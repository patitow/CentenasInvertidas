comb = sorted(set(combinations([0,1,2,3,4,5,6,7,8,9], 3)))
j=0; string=""
for i in range(0,len(comb)):
  string+= f'{comb[i]} {" "}'
  j+=1
  if(j==8):
    j=0
    string+="\n\n"
print(string)