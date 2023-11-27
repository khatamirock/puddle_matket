pattern= "jquery";s="jquery"
def maner(pattern,s):
    dict={}
    ddict={}
    s=s.split()
    print(s)
    if len(s)!=len(pattern):return False
    for x,ss in zip(pattern,s):
        
        if ss in ddict:
            if ddict[ss]!=x:return False
            continue
        else:ddict[ss]=x
        if x in dict:
            if dict[x]!=ss:return False
            else:continue
        elif x not in dict:
            dict[x]=ss

    return True

print(maner(pattern,s))