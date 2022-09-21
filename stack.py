def valid_parentheses(string):
    bracets = list(filter(lambda x: x =='(' or x == ')', string))
    stack = []

    for i in (bracets):
        
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                return False
                break
    
    if stack:
        return False
    else:
        return True

print(valid_parentheses("  (")) #False
print(valid_parentheses(")test)")) #False
print(valid_parentheses("")) #True
print(valid_parentheses("hi())(")) #False
print(valid_parentheses("hi(hi)()")) #True

