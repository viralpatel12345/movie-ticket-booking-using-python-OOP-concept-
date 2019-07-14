'''

"FairyLand Multiplex" wants to automate ticket booking and seat allocation process.

Method description:

check_seat_availability(movie_index,number_of_tickets): Checks seat availability for the given movie. Refer the code given in starter code

calculate_ticket_price(movie_index,number_of_tickets): Calculates total ticket price for the given movie. Refer the code given in starter code

generate_seat_number(movie_index,number_of_tickets): Allocate required number of seats for the given movie.
Seat numbers should be auto-generated as mentioned below:
Seat numbers should be generated starting from 1, prefixed by "M1-" for movie-1 and "M2-" for movie 2
Examples movie-1: M1-1, M1-2, M1-3 etc, movie-2: M2-1,M2-2 etc
Update total number of tickets available for the given movie in list_total_tickets
Update last seat number allocated for the given movie in list_last_seat_number
Return the list of generated seat numbers

book_ticket(movie_name,number_of_tickets): Book tickets for the given movie.
Return 0, if movie name is invalid
Return -1, if enough tickets are not available for the given movie
Else,
Generate seat numbers
Initialize attribute, seat_numbers with the list of generated seat numbers
Calculate total ticket price

Perform case sensitive string comparison.


'''

class Multiplex:
    __list_movie_name=["movie1","movie2"]
    __list_total_tickets=[100,60]
    __list_last_seat_number=[None,None]
    __list_ticket_price=[150,200]
    
    def __init__(self):
        self.__seat_numbers=None
        self.__total_price=None
    
    def calculate_ticket_price(self,movie_index,number_of_tickets):
        self.__total_price= Multiplex.__list_ticket_price[movie_index]*number_of_tickets
    
    def check_seat_availability(self,movie_index,number_of_tickets):
        if(Multiplex.__list_total_tickets[movie_index]<number_of_tickets):
            return False
        else:
            return True
    
    def get_total_price(self):
        return self.__total_price
    
    def get_seat_numbers(self):
        return self.__seat_numbers
    
    def book_ticket(self, movie_name, number_of_tickets):
        if movie_name not in Multiplex.__list_movie_name :
            return 0
        elif not(self.check_seat_availability(Multiplex.__list_movie_name.index(movie_name),number_of_tickets)) :
            return -1
        else :
            self.__seat_numbers=self.generate_seat_number(Multiplex.__list_movie_name.index(movie_name),number_of_tickets)
            self.calculate_ticket_price(Multiplex.__list_movie_name.index(movie_name),number_of_tickets)
        
    def  generate_seat_number(self,movie_index, number_of_tickets):
        l=[]
        if Multiplex.__list_last_seat_number[movie_index]==None :
           Multiplex.__list_last_seat_number[movie_index]="M"+str(movie_index+1)+"-"+str(0)
        x=int(Multiplex.__list_last_seat_number[movie_index].split('-')[1])  
           
        for k in range(0,len(Multiplex.__list_movie_name)):
          if movie_index==k :
            for i in range(x+1,x+number_of_tickets+1):
               l+=["M"+str(k+1)+"-"+str(i)]
        Multiplex.__list_total_tickets[movie_index]=Multiplex.__list_total_tickets[movie_index]-number_of_tickets
        Multiplex.__list_last_seat_number[movie_index]=l[len(l)-1]
        return l 
        
booking1=Multiplex()

status=booking1.book_ticket("movie1",10)

'''
booking5=Multiplex()
print(booking1.generate_seat_number(1,10))
print(Multiplex._Multiplex__list_total_tickets)
print(Multiplex._Multiplex__list_last_seat_number)

print(booking5.generate_seat_number(0,10))
print(Multiplex._Multiplex__list_total_tickets)
print(Multiplex._Multiplex__list_last_seat_number)
'''

if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-1")
else:
    print("Booking successful")
    print("Seat Numbers :", booking1.get_seat_numbers())
    print("Total amount to be paid:", booking1.get_total_price())
print("-----------------------------------------------------------------------------")
booking2=Multiplex()
status=booking2.book_ticket("movie2",6)
if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-2")
else:
    print("Booking successful")
    print("Seat Numbers :", booking2.get_seat_numbers())
    print("Total amount to be paid:", booking2.get_total_price())
