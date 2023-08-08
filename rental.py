import datetime

class Rental:
    def __init__(self):
        #  Our constructor class that instantiates movie rental shop.
        
        # dictionary to hold the stock of various movies
        self.stock = {}
        
    def create_stock(self, movie_name, quantity):
        # Create stock of movies
        self.stock[movie_name] = quantity
        
        
    def show_stock(self):
        # Show current movie stock
        if self.stock == {}:
            print("No movies available")
        else:
            print(f"Current movie stock : {self.stock}")
            

    def show_out_of_stock(self):
        # Show out of stock movies
        out_of_stock = {}
        stock = list(self.stock.items())
        for movie_name, quantity in stock[1:]:
            if quantity == 0:
                out_of_stock[movie_name] = quantity
        if out_of_stock == {}:
            print("All movies are in stock")
        else:
            print(f"Out of stock movies: {out_of_stock}")
            
    def check_stock(self, movie_name):
        # Check if given movie is in stock
        if movie_name in self.stock:
            if self.stock[movie_name] > 0:
                return True
            else:
                return False
        else:
            return False

    def rent_movie_hourly(self, movie_name):
        # Rent given movie per hour
        movie_name = movie_name.lower()
        if movie_name == "":
            print("Movie name required to make rental")
            return None
        elif self.check_stock(movie_name) == False:
            print(f"{movie_name} is currently out of stock")
            return None
        else:
            now = datetime.datetime.now().replace(microsecond=0)
            print("You have rented {} on hourly basis today at {} o'clock.".format(movie_name,now))
            print("You will be charged $2 for each hour.")
            print("We hope that you enjoy our service.")
            self.stock[movie_name] -= 1
            return now

    def rent_movie_daily(self, movie_name):
        # Rent given movie per day
        movie_name = movie_name.lower()
        if movie_name == "":
            print("Movie name required to make rental")
            return None
        elif self.check_stock(movie_name) == False:
            print(f"{movie_name} is currently out of stock")
            return None
        else:
            now = datetime.datetime.now().replace(microsecond=0)
            print("You have rented {} on daily basis today at {} o'clock.".format(movie_name,now))
            print("You will be charged $8 daily")
            print("We hope that you enjoy our service.")
            self.stock[movie_name] -= 1
            return now

    def rent_movie_weekly(self, movie_name):
        # Rent given movie per week
        movie_name = movie_name.lower()
        if movie_name == "":
            print("Movie name required to make rental")
            return None
        elif self.check_stock(movie_name) == False:
            print(f"{movie_name} is currently out of stock")
            return None
        else:
            now = datetime.datetime.now().replace(microsecond=0)
            print("You have rented {} on weekly basis today at {} o'clock.".format(movie_name,now))
            print("You will be charged $24 weekly")
            print("We hope that you enjoy our service.")
            self.stock[movie_name] -= 1
            return now

    def return_movie(self, request):
        # Return rented movie 
        movie_name, rentalTime, rentalBasis = request
        bill = 0

        # issue a bill only if all three parameters are not null!
        if movie_name and rentalTime and rentalBasis:
            if movie_name in self.stock:
                self.stock[movie_name] += 1
                now = datetime.datetime.now().replace(microsecond=0)
                rentalPeriod = now - rentalTime

                # hourly bill calculation
                if rentalBasis == 1:
                    bill = round(rentalPeriod.seconds / 3600) * 2

                # daily bill calculation
                elif rentalBasis == 2:
                    bill = round(rentalPeriod.days) * 20

                # weekly bill calculation
                elif rentalBasis == 3:
                    bill = round(rentalPeriod.days / 7) * 60

                print(f"Thanks for returning your {movie_name}. We hope you enjoyed the movie!")
                print("That would be ${}".format(bill))
                return bill
            else:
                print(f"You have not rented the movie {movie_name}")
                return None
        else:
            print("Are you sure you rented a movie with us?")
            return None

