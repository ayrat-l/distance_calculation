def dist_calc(expense_fuel, volume_fuel):
    stock = 20 #20 км для запаса
    dist_calc = int((volume_fuel *  100 / expense_fuel) - stock)
    return dist_calc