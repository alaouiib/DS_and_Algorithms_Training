def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    # Check if we're serving orders first-come, first-served
    if(len(served_orders) == 0):
        return True

    if(len(take_out_orders) and served_orders[0] == take_out_orders[0]):

        return is_first_come_first_served(take_out_orders[1:], dine_in_orders, served_orders[1:])
    elif(len(dine_in_orders) and served_orders[0] == dine_in_orders[0]):
        return is_first_come_first_served(take_out_orders, dine_in_orders[1:], served_orders[1:])

    else:
        return False
