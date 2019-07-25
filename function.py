from Stack import Stack

def palindrome(n):
    palindrome = True
    abc = 'abcdefghijklmnopqrstuvwxyz'
    n = n.lower()
    nospace = ''
    s = Stack()
    loc = 0
     
    for i in n:
        if i in abc:
            nospace += i
    for i in nospace:
        while loc < len(nospace)//2:
            s.push(nospace[loc])
            loc += 1
         
        if len(nospace) %2 ==1:
            loc +=1
             
        while loc < len(nospace) and palindrome:
            if s.pop() != nospace[loc]:
                palindrome = False
            loc += 1
         
             
    return palindrome