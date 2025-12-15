seps="\x00\x06\x01\x05"
print("\033c\033[40;37m\ngive me a file to mount list ? ")
i=input()
f1=open(i,"r")
ff=f1.read()
f1.close()
index=0;
ii=i.replace(".txt",".dat")
fff=ff.split(",")
f2=open(ii,"w")

names=""
for f in fff:    
    names=f
    
    f1=open(names,"r")
    g=f1.read()
    f1.close()
    g=seps+f+seps+g
    f2.write(g)
f2.write(seps)
f2.close()
