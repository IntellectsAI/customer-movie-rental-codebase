"""
This is the main function to run and test the movie rental shop.

Create customers and movies. 
Create a shop and add a stock of movies to the shop.

The customer can :
- Show the available movies currently in stock
- Rent a movie by entering the movie name and the rental condition (hourly, daily or weekly). 

The shop can:
- Issue a bill when customer decides to return the movie.
- Display available inventory
- Display out of stock movies

"""
from customer import Customer
from rental import Rental
from movie import Movie

if __name__ == '__main__':
    # create a shop
    shop = Rental()
    
    # create customers
    c1 = Customer("John McConor")
    c2 = Customer("Sarah Jackson")
    c3 = Customer("David Smith")
    
    # create movies
    m1 = Movie("star wars")
    m2 = Movie("harry potter")
    m3 = Movie("alien")
    m4 = Movie("fury")
    m5 = Movie("die hard")
    m6 = Movie("lord of the rings")
    m7 = Movie("the hobbit")
    
    # create stock of movies
    shop.create_stock(m1.name, 5)
    shop.create_stock(m2.name, 7)
    shop.create_stock(m3.name, 3)
    shop.create_stock(m4.name, 0) # out of stock movie
    shop.create_stock(m5.name, 2)
    shop.create_stock(m6.name, 4)
    shop.create_stock(m6.name, 6)
    
    # show the stock of the shop
    shop.show_stock()
    
    # show the out of stock movies
    shop.show_out_of_stock()

    # let the customer (c1 in this case) rent a movie
    movie_name = input("Enter the movie name you would like to rent : ")
    rentCondition = input("Would you like to pay hourly, daily or weekly? : ")
    c1.rent_movie(movie_name, rentCondition)
    shop.rent_movie_hourly(movie_name)
    # Now again check the stock of the shop and confirm the movie rented by the customer is discouted from the stock
    shop.show_stock()
    
    # # let the customer return the movie
    request = c1.return_movie()
    shop.return_movie(request)
    # Now again check the stock of the shop and confirm the movie returned by the customer is added back to the stock   
    shop.show_stock()
    
    