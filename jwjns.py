guests = {'1001':'Sarah', '1002':'Rucy', '1003':'Jessy', '1004':'Minsu', '1005':'jihye'}
appetizers = {'1001':'Salmon Salad', '1002':'Seafood Salad', '1003':'Potato Soup'} 
main_courses = {'2001':'Hawaiian Pizza', '2002':'Teriyaki Chicken','2003':'Pork Steak'} 
desserts = {'3001':'Cookie and Cream cake', '30002':'Strawberry Icecream', '3003':'Fruit Smoothie'}

#Dictionary with the customer's order
order = {}

room = None
#check if the room is registered
while room not in guests.keys():
    room = input('your room number: ')
    #check if room exists
    
    if room in guests.keys():
        name = input('your name: ')
        #Check if the room and guest name match
        
    if guests[room] != name:
        print ('Your name does not exist.')
        room = None
            
    else:
        print (f'Room {room} is not registered.')
        

def select_food (food_type, food_dict):
    #Print food
    print ()
    print (f'{food_type} menu')
    print ('------------------------------------')
    for code, food in food_dict.items():
        print (code, '->', food)

    #Select food
    food_code = None
    #validate the food
    while food_code not in food_dict.keys():
        food_code = input ('Please, enter the appetizer code: ')
        if food_code not in food_dict:
            print('Wrong appetizer code.')
        else:
            return {food_code: food_dict[food_code]}

#Appetizers
order.update(select_food ('Appetizers', appetizers))
#Main course
order.update(select_food ('Main Courses', main_courses)) 
#Dessert
order.update(select_food ('Desserts', desserts)) 

#Validate the delivery time
validtime = False
timeformat = "H:M"
while not validtime:
    delivery_time = input("delivery time (hh:mm): ")
    try:
        validtime = datetime.datetime.strptime(delivery_time, timeformat)
    except ValueError:
       print ('Time format hh:mm')
