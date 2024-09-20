

def is_prime(num):
       num = int(num)
       if num == 1 or num == 2 or num == 3:
              return print("its a prime number"),True
       for i in range(2,num-1):
              if num % i == 0:
                     return print("its not a prime"),False
       return print("its a prime number"),True   

def is_even(num):
       if num == 1:
              print('its odd number'), False
       if num % 2 == 0:
              return print("its even number"), True
       return print('its odd number'), False  


def div_by_five(num):
       if num % 5 == 0:
               print('divide by 5 without remain')
       else:   
              print('divide by 5 with remain')  

def calculate(result):
       print(result)
       is_prime(result)
       is_even(result)
       div_by_five(result)
       print()

def operator_validator(operation):
       operations = ['1', '2', '3','4', '5', '6', '7']
       for i in operations:
              if i == operation:
                     return True
       else: return False
                       

def switch(operation, num1, num2):
            
            if operation == '1':
                    result = num1 + num2
                    calculate(result)

            elif operation == '2':
                    result = num1 - num2
                    calculate(result)
                    
            elif operation == '3':
                   result = num1 * num2 
                   calculate(result)

            elif operation == '4':
                   result = num1 / num2
                   calculate(result)

            elif operation == '5':
                    result = pow(num1, num2)
                    calculate(result)       

            elif operation == '6':
                    result = num1 % num2 
                    calculate(result)

            elif operation == '7':
                    quit()


def main():
    print("Welcome to python calculator")
    
    
    operation = ""
    while operation != '7':
            print('choose an operator to calculate: ')
            operation = input("1-Add, 2-Subtract, 3-Multiply, 4-Divide, 5-Power of, 6-Modulos, 7-Exit:  ")

            while not operator_validator(operation):
                    print()
                    print("please enter correct choice from below")
                    operation = input("1-Add, 2-Subtract, 3-Multiply, 4-Divide, 5-Power of, 6-Modulos, 7-Exit:  ")
                    
            #handle validate number input
            while True and operation.upper() != '7':
                  try:
                       num1 = int(input('please choose number 1: '))    
                       num2 = int(input('please choose number 2: '))
                           
                  except:
                         print('please enter numbers only!')
                         continue
                  else: break
                      

            switch(operation, num1, num2)                           
                
            
                                               
                        
                    
main()         
