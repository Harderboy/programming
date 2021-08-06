'''
滴滴：出行技术/质量效能/服务端技术QA/开放平台QA 
面试题
    输入：3a%zvssOO8n*bbAAA
    输出：AObsvz
        A:3
        O:2
        s:2
'''

str=input("输入任意长度字符串：")
list=[]
for i in str:
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