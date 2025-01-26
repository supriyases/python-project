class CoffeeShop: 
    def __init__(self):

        self.menu = {
            
            "Espresso": 3.00,

            "Americano": 3.50,

            "Latte": 4.00,

            "Cappuccino": 4.50,

            "Mocha": 4.75
        }


        self.order = {}

        def display_menu(self):

            print("\n---coffee Menu---")

            for coffee, price in self.menu.items():

                print(f"{coffee}: ${price}")

        def take_order(self):

            print("\nEnter the coffee you'd like to order (or type 'done' to finish):")

            while True:

                coffee = input("Coffee Name: ").captialize()
                
                if coffee == "Done":

                    break

                elif coffee in self.menu:

                    quantify = int(input(f"How many {coffee}s would you like? "))

                    if coffee in self.order:

                        self.order[coffee] += quantity

                    else:

                        self.order[coffee] = quantity

                else:

                    print("sorry, we don't have that coffee. please choose from menu.")

        def calculate_total(self):

            total = 0

            for coffee, quantity in self.order.items():

                total += self.memu[coffee] * quantity

            return total

        def print_receipt(self):

            print("\n--- Receipt ---")

            for coffee, quantity in self.order.items(): 

                print(f"{coffee} x{quantity} = ${self.menu[coffee] * quantity:.2f}")

            print(f"\nTotal: ${self.calculate_total():.2f}")   

def main():

    coffee_shop = CoffeeShop() 

    while True:

        print("\nWelcome to the coffee shop!")

        coffee_shop.display_menu() 
        coffee_shop.take_order()   
        coffee_shop.print_receipt()

        another_order = input("\nWould you like to order something else? (yes/no): ").lower()

        if another_order != "yes":

            print("\nThank you for visiting our coffee shop!")

            break

if __name__ == "__main__":

 main()        
        



    




