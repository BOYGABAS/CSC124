'''
Isaiah Andre Pabillon
BSCS-2
2018-5769

Algorithm:

    1) Create an empty list to be filled with random elements

    2) Set a random range from 0 to 25 and add it to the ASCII equivalent of
      "A" to produce random letters from "A" to "Z" and append it to the empty list

    3) Repeat step #2 at your leisure

    4) Ask user to select which sorting algorithm to perform

        4.1) If user inputs "1" then perform insertion sort

        4.2) If user inputs "2" or any string if the user is bored, then perform merge sort

        Insertion sort:

            1) Create a new empty list

            2) Scan through the elements of the scrambled list

                2.1) If the new list is empty then simply append element

                2.2) Else compare them to the elements of the new list and declare a variable
                    for the index that will start iterating

                    2.2.1) If the current element in the scrambled list is greater than the
                          element of the new list, then move to the next element via incrementing
                          the index variable

                    2.2.2) Else add/insert the element from the scrambled list to the new list
                           at the index[variable]

            3) Display the new list

        Merge sort:

            1) Allocate three lists which are left,right and final

            2) Browse through the scrambled list and append them to the new lists accordingly

                2.1) If the element's index is at the lower half of the list then assign to left list

                2.2) Else assign it to the right list

            3) With the left and right lists, do step #1

            4) If the list came to a point where there is only 1 element, return as a list

            5) Sort the elements of the two lists by scanning their elements and appending the lesset one
              to the final list and the list with the lesser element will select the next element in its list

            6) If one side of the lists are already finished, append the remaining elements of the other list
              to the final list as they are already the later/bigger items since they are already sorted

            7) Repeat until sorted and print output



'''
import random
import time

def insertionsort(arg,arglist):
    for indeks in range(len(arglist)):
        if (arg)<=(arglist[indeks]) or indeks==len(arglist)-1:
            return indeks

def mergesort(arglist):
    if len(arglist)<=1:
        return arglist
    arglistleft=[]
    arglistright=[]
    j=0
    length=len(arglist)
    if length%2==0:
        length=int(length/2)
    else:
        length=int((length/2)-0.5)
    for i in arglist:
        if j<=length:
            arglistleft.append(i)
        else:
            arglistright.append(i)
        arglist.pop(0)
        j+=1
    arglistright=mergesort(arglistright)
    arglistleft=mergesort(arglistleft)
    L=len(arglistleft)
    R=len(arglistright)
    l=0
    r=0
    while l<L and r<R:#while len(arglistleft)>0 or len(arglistright)>0:
        if (arglistleft[0])<=(arglistright[0]):
            arglist.append(arglistleft[l])
            l+=1
            #arglistleft.pop(0)
        else:
            arglist.append(arglistright[r])
            r+=1
            #arglistright.pop(0)
    #if len(arglistleft)==0:
    if l==L:
        arglist.extend(arglistright)
    else:
        arglist.extend(arglistleft)
    #print(arglist)
    return arglist

def mergesortpart2(arglist):
        if len(arglist)<=1: #This is the point where we reached the single item where it can't be split
            return arglist
        else:
            left=[]
            right=[]
            final=[]
            for i in range(len(arglist)): #This is where the elements in the list will either be assigned left or right
                if i<=(len(arglist)/2)-1:
                    left.append(arglist[i])
                else:
                    right.append(arglist[i])
            left=mergesortpart2(left) #This is where we split the already spltted lists
            right=mergesortpart2(right)
            while len(left)>0 and len(right)>0: #This is the sorting part
                if left[0]<right[0]:
                    final.append(left[0])
                    left.pop(0)
                else:
                    final.append(right[0])
                    right.pop(0)
            if len(left)==0: #If one side of the list is finished then slam the other list to the end of the sorted list as it is logically already sorted
                final.extend(right)
            else:
                final.extend(left)
            return final #return the sorted list

LETTERTONUMBER=ord("A") # Setting a basis for conerting random numbers to their respective element in the alphabet
elements=1
xaxis=[]
yaxisinsert=[]
yaxismerge=[]
scrambledlist=[]
sortlist=[]
while elements<10000:
    elements*=10
    for i in range(0, elements): #The scrambled list will be filled with 5 random letters
        scrambledlist.append(int(random.randint(0,elements))) # This will append the converted random numbers to letters
    #print(scrambledlist)
    #print("\n1) Insetion sort\n2) Merge sort")
    #inpot=input("> ")

    if True:#inpot=="1":
        '''
        The next two lines are excluded from the loop so that the program wouldn't have to check the conidtion
        if the new list is empty in every iteration
        '''
        past=time.time()
        sortlist.append(scrambledlist[0])
        #scrambledlist.pop(0)
        indekser=0
        for indeks in scrambledlist:
            sortlist.insert(insertionsort(indeks,sortlist),indeks)
            #print(sortlist)
            '''
            Supposedly the program will print out the final list only but I decided to emphasize the process
            of the insertion sort so the program will print the list for every iteration of the insertion sort
            which is shown in the following lines in this current loop and the indekser=0 in the current condition
            '''
            scrambledlist.pop(indekser)
            scrambledlist.insert(insertionsort(indeks,sortlist),indeks)
            indekser+=1
            #print("insert:",scrambledlist)
        yaxisinsert.append(time.time()-past)
        #print(scrambledlist)

    if True:#else: #if user inputs 2 or anything else, the program will automatically perform merge sort
        past=time.time()
        scrambledlist=mergesortpart2(scrambledlist)
        yaxismerge.append(time.time()-past)
        #print(scrambledlist)
        '''
        The process of merge sorting would be uncomfortable to
        trace if presented linearly(not in a tree). So I decided
        to display only the final output
        '''
    scrambledlist.clear()
print(yaxisinsert)
print(yaxismerge)
