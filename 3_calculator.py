try: 
   a = int(input("Enter the first number: "))
   b = int(input("Enter the second number: "))

   print("Choose a following operator:\n + for addition\n - for substraction\n * for multiplication\n / for division")

   var = input("Enter the operator: ")
   match var:
      case "+":
         print(f"The result is {a + b}")
      case "-":
         print(f"The result is {a - b}") 
      case "*":
         print(f"The result is {a * b}") 
      case "/":
         print(f"The result is {a / b}") 
      case default:
         print("check the correct values.")   
    
except:
   print("Enter valid values for a and b")