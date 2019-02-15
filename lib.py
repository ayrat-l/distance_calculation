def dist_calc(expense_fuel, volume_fuel):
    """
    >>> dist_calc(10,20)
    180
    """
    stock = 20 #20 км для запаса
    dist_calc = int((volume_fuel *  100 / expense_fuel) - stock)
    return dist_calc