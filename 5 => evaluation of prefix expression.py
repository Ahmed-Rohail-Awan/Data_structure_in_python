#program to evaluate a prefix expression

#to check if the given character is operand
def check_for_operand(c):
    return c.isdigit()

#function to evaluate the given prefix exopression
def evaluation_of_prefix(expression):
    stack = []
    
    #to iterate over string in reverse order
    for x in expression[::-1]:
        if check_for_operand(x):
            stack.append(int(x))
    #pop values from the stack and calculate result and also pus the result back into stack agin        
        else:
            o1 = stack.pop()
            o2 = stack.pop()
        
            if x == '+':
                stack.append(o1 + o2)         
            if x == '-':
                stack.append(o1 - o2)
            if x == '*':
                stack.append(o1 * o2)
            if x == '/':
                stack.append(o1 / o2)
    return stack.pop()
            
    
    # Example

expression = "+9*26"
print(evaluation_of_prefix(expression))
