import orders
    
def main():
    menu = { ' Burger Spam': 4.50, ' Burger Spam': 4.50,' Burger Spam': 4.50, }
    orders.print_menu(menu)
    orders = orders.get_order(menu)
    total = orders.bill_total(orders, menu)
    print ('You ordered:', order, 'Total:', total)
    
main()