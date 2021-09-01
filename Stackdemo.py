from Stack import*

def main():
    stack1 = Stack(1000)
    stack2 = Stack(1000)

    operations = ['=','<','>']
    while(True):
        if not stack1.is_empty():
            print("current at page:",stack1.peek())
        
        operater = input("Please operate your browser: \n1.'=' to type a new URL\n2.'<' to backward the last page\n3.'>' to forward the last page\n")
        if operater not in operations: 
            print("invalid operation!")
            break

        if operater == '=':
            url = input("Please type URL: ")
            stack1.push(url)
        elif operater == '<':
            if not stack1.is_empty():
                stack2.push(stack1.pop())
                
        elif operater == '>':
            if not stack2.is_empty():
                stack1.push(stack2.pop())
                
main()