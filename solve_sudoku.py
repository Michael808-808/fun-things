import test_matrices

def solve(x):
    '''
    x is a 2d list representing a sudoku puzzle

    returns: a 2d list representing the solved puzzle or prints "impossible"
    if x is not a valid sudoku puzzle
    '''
    assert len(x)==9, "the input sudoku matrix is invalid"
    for i in x:
        assert len(i)==9, "the input sudoku matrix is invalid"
        for j in i:
            assert type(j)==int or j==None, "sudoku matrices must be composed of ints in range[1..9] or None"
    keys=[]
    row_mod=0
    col_mod=0
    for i in range(9):
        if i!=0 and i%3==0:
            row_mod+=3
        for j in range(3):
            for k in range(3):
                keys.append((j+row_mod,k+col_mod%9))
        col_mod+=3
    indict={}
    for i in range(len(keys)):
        indict[keys[i]]=None
    for i in indict.keys():
        indict[i]=x[i[0]][i[1]]
    mod=0
    box_keys=[]
    while mod<9:
        z=list(indict.keys())
        temp=z[mod*9:mod*9+9]
        box_keys.append(temp)
        mod+=1

    r=0
    while not check_finished(indict) and r<1000:
        elimination(indict, box_keys)
        r+=1
    print(r)
    return list_convert(indict)

def elimination(indict, box_keys):
    for key in indict.keys():
        if type(indict[key])!=int:
            #check which numbers are not present in the same row, column, and box.
            #Replace None with list of possible numbers
            a=scan_row(key, indict)
            b=scan_column(key, indict)
            c=scan_box(key, indict, box_keys)
            d=list(set(list(set(a).intersection(set(b)))).intersection(set(c)))
            if len(d)==1:
                indict[key]=d[0]
            else:
                indict[key]=d
    scan_box2(indict,box_keys)
    scan_row2(indict)
    scan_column2(indict)

def scan_row(x,tempdict):
    #x is a tuple representing the index of the box being compared to its row
    #tempdict is the dictionary representing the sudoku matrix
    nums=[1,2,3,4,5,6,7,8,9]
    row_keys=[]
    for j in tempdict.keys():
        if j[0]==x[0]:
            row_keys.append(j)
    for k in row_keys:
        if tempdict[k] in nums:
            nums.remove(tempdict[k])
    return nums

def scan_column(x,tempdict):
    nums=[1,2,3,4,5,6,7,8,9]
    col_keys=[]
    for j in tempdict.keys():
        if j[1]==x[1]:
            col_keys.append(j)
    for k in col_keys:
        if tempdict[k] in nums:
            nums.remove(tempdict[k])
    return nums

def scan_box(x,tempdict,box_keys):
    nums=[1,2,3,4,5,6,7,8,9]
    box_ind=None
    for i in range(len(box_keys)):
        if x in box_keys[i]:
            box_ind=i
    b_keys=box_keys[box_ind]
    for k in b_keys:
        if tempdict[k] in nums:
            nums.remove(tempdict[k])
    return nums

def scan_box2(tempdict,box_keys):
    for i in box_keys:
        unk_list=[]
        for j in i:
            if type(tempdict[j])==list:
                unk_list.append(j)
        nums=list(range(1,10))
        for k in i:
            if type(tempdict[k])==int:
                nums.remove(tempdict[k])
        for l in nums:
            count=0
            ind=[]
            for m in unk_list:
                if type(tempdict[m])==list and l in tempdict[m]:
                    count+=1
                    ind.append(m)
            if count==1:
                tempdict[ind[0]]=l

def scan_row2(tempdict):
    rows=list(range(1,10))
    for i in rows:
        row_tuples=[]
        for j in tempdict.keys():
            if j[0]==i:
                row_tuples.append(j)
        row_unknowns=list(range(1,10))
        unknown_boxes=[]
        for k in row_tuples:
            if type(tempdict[k])==int:
                row_unknowns.remove(tempdict[k])
            else:
                unknown_boxes.append(k)
        for l in row_unknowns:
            count=0
            ind=[]
            for m in unknown_boxes:
                if type(tempdict[m])!=int and l in tempdict[m]:
                    count+=1
                    ind.append(m)
            if count==1:
                tempdict[ind[0]]=l

def scan_column2(tempdict):
    cols=list(range(1,10))
    for i in cols:
        col_tuples=[]
        for j in tempdict.keys():
            if j[1]==i:
                col_tuples.append(j)
        col_unknowns=list(range(1,10))
        unknown_boxes=[]
        for k in col_tuples:
            if type(tempdict[k])==int:
                col_unknowns.remove(tempdict[k])
            else:
                unknown_boxes.append(k)
        for l in col_unknowns:
            count=0
            ind=[]
            for m in unknown_boxes:
                if type(tempdict[m])!=int and l in tempdict[m]:
                    count+=1
                    ind.append(m)
            if count==1:
                tempdict[ind[0]]=l

def check_finished(indict):
    for key in indict.keys():
        if indict[key]==None or type(indict[key])==list:
            return False
    return True

def list_convert(indict):
    empty=[['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','','']]
    for i in indict.keys():
        empty[i[0]][i[1]]=indict[i]
    return empty

done1=solve(test_matrices.x1)
print(done1==test_matrices.fin1)

done2=solve(test_matrices.x2)
print(done2==test_matrices.fin2)

done3=solve(test_matrices.x3)
print(done3==test_matrices.fin3)

done4=solve(test_matrices.x4)
print(done4==test_matrices.fin4)

done_hard1=solve(test_matrices.hard1)
print(done_hard1==test_matrices.finhard1)

done_hard2=solve(test_matrices.hard2)
print(done_hard2)
print(done_hard2==test_matrices.finhard2)
