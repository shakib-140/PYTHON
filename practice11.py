# practice question_1 :

# import math as m
# b=input('enter a value as input :')
# a=float(b)
# print(f'the ceil value of input is :{m.ceil(a)}')
# print(f'the floor value of input is :{m.floor(a)}')




# practice question_2 :

# num_1=int (input('enter the value of first integer input :'))
# num_2=int (input('enter the value of second integer input :'))
# num_3=int (input('enter the value of third integer input :'))
# if num_1 >=0 :
#     print(num_1)
# else :
#     print(-1*num_1)    
# if num_2 >=0 :
#     print(num_2)
# else :
#     print(-1*num_2)
# if num_3 >=0 :
#     print(num_3)
# else :
#     print(-1*num_3)         





# #practice question_3 : 

# player_1=input('player_1 input any one of these "rock","paper","scissors" :')
# if player_1=="rock" or player_1=="paper" or player_1=="scissors" :
#     player_2=input('player_2 input any one of these "rock","paper","scissors" :')
#     if player_2=="rock" or player_2=="paper" or player_2=="scissors" :
       
#        if player_1=="rock" and player_2=="paper" :
#           print("player_2 is win")  
#        elif player_1=="rock" and player_2=="scissors" :
#          print("player_1 is win")

#        elif player_1=="paper" and player_2=="rock" :
#           print("player_1 is win")
#        elif player_1=="paper" and player_2=="scissors" :
#           print("player_2 is win")

#        elif player_1=="scissors" and player_2=="paper" :
#           print("player_1 is win")
#        elif player_1=="scissors" and player_2=="rock" :
#           print("player_2 is win")
 

#        else :
#          print("tie")
#     else :
#          print('invalid input of player_2 try again with valid input ')   
    
# else :
#     print('invalid input of player_1 try again with valid input ')
    




        
# practice question_4 :

# while True :
#   n=(input('enter a value as input :'))
#   if n=="quit" :
#    break
#   m=int(n)
#   if m>0 :
#     print('it is a posiive number')
#   elif m<0 :
#    print('it is a negative number')
#   else :
#     print('it is zero')




#practice question_5 :

# n=1
# while n<=15 :
#     if n%3==0 and n%5==0 :
#         print("fizzbuzz")
#     elif n%3==0 :
#         print('fizz')
#     elif n%5==0 :
#         print('buzz')
#     else :
#      print(n)
#     n=n+1

#practice Question_6 :

for row in range(5) :
    for col in range(5):
        if col==0 or col==4 or (row==2 and (col==1 or col==3)) or (row ==3 and col==2):
            print('*',end=" ")
        else :
            print(" ",end=" ")
    print("\n")    




# result_str = ""

# for row in range(0, 7):

#     for column in range(0, 7):

#         if (column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4)) or (row == 3 and column == 3)):
#             result_str = result_str + "* "  
#         else:
#             result_str = result_str + "  " 

#     result_str = result_str + "\n"  

# print(result_str)




