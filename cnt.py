a={'Alex': ['subj1', 'subj2', 'subj3'],'David': ['subj1', 'subj2']}
c=0
for x,y in a.items():
    for i in y:
        c=c+1
print(c)