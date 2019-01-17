# import the necessary dependencies
from pizzapy import *
from twilio_send_message import send_message

def order_pizza():
    try:
        customer = Customer('Barack', 'Obama', 'barack@whitehouse.gov', '2024561111', '700 Pennsylvania Avenue NW, Washington, DC, 20408')
        closest_dominos = StoreLocator.find_closest_store_to_customer(customer)
        
        menu = closest_dominos.get_menu()
        print("search the menu for coke, because you're cheap :)")
        menu.search(Name='Coke')

        order = Order.begin_customer_order(customer, closest_dominos)
        order.add_item('20BCOKE')

        card = CreditCard('4100123422343234', '0115', '877', '90210')

        order.place(card)
        closest_dominos.place_order(order, card)

        send_message("Pizza has been ordered")
        
    except Exception as e:
        print("Exception",e,"\n","Pizza has not been ordered.")
        send_message("Pizza has not been ordered")

if __name__ == "__main__":
    order_pizza()