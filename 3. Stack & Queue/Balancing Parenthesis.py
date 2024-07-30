
def balancingParanthesis(s):
    l=[]
    if len(s)%2==1:
        print("Not Balanced")
        return
    for i in range(0, len(s)):
        if s[i] in "{([":
            l.append(s[i])
        else:
            if s[i]=="]" and l[-1]=="[":
                l.pop(-1)
            elif s[i]==")" and l[-1]=="(":
                l.pop(-1)
            elif s[i]=="}" and l[-1]=="{":
                l.pop(-1)
    if l==[]:
        print("Balanced")
    else:
        print("Not Balanced")

s=input()
balancingParanthesis(s)