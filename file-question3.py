banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"] 
i=0
while i<len(banks_list):
    a=banks_list[i]+" "+"\n"
    f=open("file-question3.txt","a",)
    f.write(a)
    f.close()
    i=i+1
# f=open("file-question3.txt","a")
# f.write(a)
# f.close()
f=open("file-question3.txt","r")
print(f.read())
