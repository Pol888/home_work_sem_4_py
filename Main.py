# task 1

def matrix_transposition(mtrx: list) -> list:
    new_matrix = [[0] * len(matrix) for _ in range(len(matrix[0]))]
    for i in range(len(mtrx[0])):
        for j in range(len(mtrx)):
            new_matrix[i][j] = mtrx[j][i]

    return new_matrix


matrix = [[1, 2], [5, 6], [0, 2]]
matrix_2 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

print(matrix_transposition(matrix))
# -----------------------------------------------------------------------------------------------------
# task 2

def function_key_to_value(**kwargs) -> dict:
    new_dict = {}
    for key, val in kwargs.items():
        if type(val) == list or type(val) == bytearray or type(val) == dict or type(val) == set:
            new_dict[str(val)] = key
            continue
        new_dict[val] = key
    return new_dict


print(function_key_to_value(t=[1, 3], k=9))
# ----------------------------------------------------------------------------------------------------
# task 3 (банкомат)

# Задание №6
# -Напишите програнму банкомат.
# -У Начальная сумма равна нулю
# / -Допустимые действия: пополнить, снять, выйти
# //  2 Сумма пополнения и снятия кратны 50 у.е.
# У 2 Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# У  2 После каждой третей операции пополнения или снятия начисляются проценты - 5%
# У2  Нельзя снять больше, чем на счёте
# У  1 При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# у Любое действие выводит сумму денег т
import datetime

def main():
    initial_amount = 0                 # начальная сумма
    count_operations_replenishment = 0 # счетчик операций
    list_operations = []
    menu(initial_amount, count_operations_replenishment, list_operations)

def print_account_amount(sum):   # печать суммы на счете
    print(f'Сумма на счете = {sum}')

def wealth_order(init_amount, list_o:list):
    if init_amount > 5000000:  # налог на богатство перед операцией
        init_amount -= init_amount / 100 * 10
        print('Сработал налог на богатство')
        print_account_amount(init_amount)
        list_o.append(f'налог на богатство 10%, сумма на счете {init_amount}, {datetime.datetime.now()}')
        return init_amount, list_o
    return init_amount, list_o

def multiplicity_check(r_amount):   # проверяет кратность 50
    if r_amount % 50 == 0:
        return False
    return True

def withdrawal(init_amaunt, withdrawal_amount, count_operations_replenishment, list_o):
    if withdrawal_amount < 30 or withdrawal_amount > 600:  # снятие без процентов
        if init_amaunt - withdrawal_amount < 0:
            print('Снятие невозможно, сумма снятия превышает сумму на счете')
            print_account_amount(init_amaunt)
        else:
            init_amaunt -= withdrawal_amount
            list_o.append(f'Снятие без процентов {withdrawal_amount}$, сумма на счете{init_amaunt}, '
                          f'{datetime.datetime.now()}')
            print_account_amount(init_amaunt)
            count_operations_replenishment += 1
            if count_operations_replenishment % 3 == 0:
                init_amaunt -= init_amaunt / 100 * 5
                print_account_amount(init_amaunt)
                list_o.append(f'Снятие 5% за каждую 3-тью операцию, сумма на счете{init_amaunt}, '
                              f'{datetime.datetime.now()}')
                return init_amaunt, count_operations_replenishment, list_o
        return init_amaunt, count_operations_replenishment, list_o

    else:  # снятие с процентами
        if init_amaunt - withdrawal_amount + (withdrawal_amount / 100 * 1.5) < 0:
            print('Снятие невозможно, сумма снятия превышает сумму на счете')
            print_account_amount(init_amaunt)
        else:
            init_amaunt -= withdrawal_amount + (withdrawal_amount / 100 * 1.5)
            list_o.append(f'Снятие с процентами {withdrawal_amount + (withdrawal_amount / 100 * 1.5)}$, '
                          f'сумма на счете{init_amaunt}, '
                          f'{datetime.datetime.now()}')
            print_account_amount(init_amaunt)
            count_operations_replenishment += 1

            if count_operations_replenishment % 3 == 0:
                init_amaunt -= init_amaunt / 100 * 5
                list_o.append(f'Снятие 5% за каждую 3-тью операцию, сумма на счете{init_amaunt}, '
                              f'{datetime.datetime.now()}')
                print_account_amount(init_amaunt)
                return init_amaunt, count_operations_replenishment, list_o
        return init_amaunt, count_operations_replenishment, list_o

def replenishment(init_amaunt, withdrawal_amount, count_operations_replenishment, list_o):
    init_amaunt += withdrawal_amount  # пополнение
    print_account_amount(init_amaunt)
    count_operations_replenishment += 1
    list_o.append(f'Пополнение на сумму {withdrawal_amount}$, '
                  f'сумма на счете{init_amaunt}, '
                  f'{datetime.datetime.now()}')

    if count_operations_replenishment % 3 == 0:
        init_amaunt -= init_amaunt / 100 * 5
        print_account_amount(init_amaunt)
        list_o.append(f'Снятие 5% за каждую 3-тью операцию, сумма на счете{init_amaunt}, '
                      f'{datetime.datetime.now()}')
        return init_amaunt, count_operations_replenishment, list_o
    return init_amaunt, count_operations_replenishment, list_o


def menu(initial_amount, count_operations_replenishment, list_o):
    flag = True
    while flag:
        print_account_amount(initial_amount)  # печать суммы
        action = input('1 - пополнить\n2 - снять\n3 - лист операций\n(любой знак) - выйти\n')
        if action == '1':
            flag_2 = True
            while flag_2:
                initial_amount, list_o = wealth_order(initial_amount, list_o)  # налог на богатство перед операцией
                replenishment_amount = int(input('Введите сумму пополнения кратную 50\n'))  # ввод суммы
                if multiplicity_check(replenishment_amount):  # проверка кратности
                    print('Сумма не кратная 50')
                    print_account_amount(initial_amount)
                else:
                    initial_amount, count_operations_replenishment, list_o = replenishment(initial_amount, replenishment_amount,
                                                                                   count_operations_replenishment, list_o)
                flag_2 = False

        elif action == '2':
            flag_2 = True
            while flag_2:
                initial_amount, list_o = wealth_order(initial_amount, list_o)  # налог на богатство перед операцией
                withdrawal_amount = int(input('Введите сумму снятия кратную 50\n'))
                if multiplicity_check(withdrawal_amount):  # проверка кратности
                    print('Сумма не кратная 50')
                    print_account_amount(initial_amount)
                else:
                    initial_amount, count_operations_replenishment, list_o = withdrawal(initial_amount, withdrawal_amount,
                                                                                count_operations_replenishment, list_o)
                flag_2 = False

        elif action == '3':
            print(list_o)

        else:
            flag = False





if __name__ == '__main__':
    main()