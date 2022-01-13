import pdb

str="dasfjkahdf"
list=[]
for i in str:
    pdb.set_trace()
    if 65<=ord(i)<=90 or 97<=ord(i)<=122 :
        list.append(i)

print("".join(sorted(set(list),key=ord)))

dict={}
for j in sorted(list,key=ord):
    if j in dict:
        dict[j]+=1
    else:
        dict[j]=1

for k,v in dict.items():
    if v>=2:
        print(k,":",v)