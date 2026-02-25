from sstack import Stack

#bracket matching problem

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

#infix to postfix
def infix_postfix(expression):
    precedence = {'+':1,'-':1,'*':2,'/':2}
    s = Stack()          # using Stack instead of list
    output = ''

    for char in expression:
        if char == ' ':
            continue
        if char.isalnum():
            output += char

        elif char == '(':
            s.push(char)

        elif char == ')':
            while not s.is_empty() and s.peek() != '(':
                output += s.pop()
            s.pop()     # remove '('

        else:   # operator
            while (not s.is_empty() and 
                   s.peek() != '(' and 
                   precedence[char] <= precedence.get(s.peek(), 0)):
                output += s.pop()
            s.push(char)

    while not s.is_empty():
        output += s.pop()

    return output



#postfix evaluation
def postfix_evaluation(expression):
    tokens = expression.split()
    operators = ['+', '-', '*', '/']
    s = Stack()   
    for token in tokens:
        if token.isdigit():
            s.push(int(token))

        elif token in operators:
            op1 = s.pop()
            op2 = s.pop()

            if token == '+':
                res = op2 + op1
            elif token == '-':
                res = op2 - op1
            elif token == '*':
                res = op2 * op1
            elif token == '/':
                res = op2 / op1

            s.push(res)

    return s.pop()





print("Parenthesis:", bracket("([{}])"))
print("Infix to Postfix:", infix_postfix("3 + 5 * 2"))
print("Postfix:", postfix_evaluation("3 5 + 2 *"))

