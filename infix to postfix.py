from sstack import Stack

def bracket(expression):
    s = Stack()

    opening = ['[','{','(']
    closing = [')','}',']']
    pair = {']':'[','}':'{',')':'('}

    for char in expression:
        if char in opening:
            s.push(char)
        elif char in closing:
            if s.is_empty() or s.pop() != pair[char]:
                print('unbalanced')
                return

    if s.is_empty():
        print('balanced')
    else:
        print('unbalanced')


exp1 = '[({})]'
exp2 = '[[])]'

bracket(exp2)
bracket(exp1)
