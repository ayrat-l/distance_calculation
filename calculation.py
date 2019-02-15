from lib import dist_calc

expense_fuel = int(input('Введите средний расход на 100 км >> '))
volume_fuel = int(input('Введите остаток топлива в баке >> '))

print('Через', dist_calc(expense_fuel, volume_fuel), 'км закончится топливо. Не забудьте заправиться!')