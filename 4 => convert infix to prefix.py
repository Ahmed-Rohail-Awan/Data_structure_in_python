#function to convert infix to prefix


#check whether it is operator or operand
def check_for_operator(c):
    return(not(c>='a' and c<='z') and not(c>='0' and c<='9') and not(c>='A' and c<='Z'))


#definiing priority
def operator_priority(p):
    if(p=='-'  or p=='+'):
        return 1
    elif(p=='*' or p=="/"):
        return 2
    elif (p=='^'):
        return 3
    return 0


#function to convert infix to preffix
def infixtoprefix(infix_exp):
    #stack for operator and operands
    operators=[]       
    operands=[]
    
    #if current characer is a opening bracket then push it into the operator stack
    for i in range(len(infix_exp)):
        if (infix_exp[i]=='('):
            operators.append(infix_exp[i])
            
        #if current characer is a closing bracket then pop from both stack and push result in operand stack     
        elif (infix_exp[i]==')'):
            while (len(operators)!=0 and operators[-1] != '('):
                
                operand1=operands[-1]     #1st operand
                operands.pop()
                
                operand2=operands[-1]     # 2nd operand 
                operands.pop()
                
                operator=operators[-1]    # operator
                operators.pop()
                
                result = operator + operand2 + operand1
                operands.append(result)
            operators.pop()
            
        # if current charter is an operand then push it into operand stack    
        elif (not check_for_operator(infix_exp[i])):
            operands.append(infix_exp[i]+ "")
        
        #if current character is an operator then push it into operator stack and result in operand stack
        else:
            while(len(operators)!=0 and operator_priority(infix_exp[i]) <= operator_priority(operators[-1])):
                operand1=operands[-1]     #1st operand
                operands.pop()
                
                operand2=operands[-1]     # 2nd operand 
                operands.pop()
                
                operator=operators[-1]    # operator
                operators.pop()
                            
                result = operator + operand2 + operand1
                operands.append(result)
            operators.append(infix_exp[i])
            
    #pop operator from operator stack until it is empty and also add result of each pop operand stack
    while(len(operators)!=0):
                operand1=operands[-1]     #1st operand
                operands.pop()
                
                operand2=operands[-1]     # 2nd operand 
                operands.pop()
                
                operator=operators[-1]    # operator
                operators.pop()
                            
                result = operator + operand2 + operand1
                operands.append(result)
    return operands[-1]
  
  
 # examples 
s = "(A-B/C)*(D/E-F)"
print( infixtoprefix(s))
