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

#print(matrix_transposition(matrix))
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


# print(function_key_to_value(t=[1, 3], k=9))
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


def main():
    initial_amount = 0                 # начальная сумма
    count_operations_replenishment = 0 # счетчик операций
    menu(initial_amount, count_operations_replenishment)

def print_account_amount(sum):   # печать суммы на счете
    print(f'Сумма на счете = {sum}')

def wealth_order(init_amount):
    if init_amount > 5000000:  # налог на богатство перед операцией
        init_amount -= init_amount / 100 * 10
        print('Сработал налог на богатство')
        print_account_amount(init_amount)
        return init_amount
    return init_amount

def multiplicity_check(r_amount):   # проверяет кратность 50
    if r_amount % 50 == 0:
        return False
    return True

def withdrawal(init_amaunt, withdrawal_amount, count_operations_replenishment):
    if withdrawal_amount < 30 or withdrawal_amount > 600:  # снятие без процентов
        if init_amaunt - withdrawal_amount < 0:
            print('Снятие невозможно, сумма снятия превышает сумму на счете')
            print_account_amount(init_amaunt)
        else:
            init_amaunt -= withdrawal_amount
            print_account_amount(init_amaunt)
            count_operations_replenishment += 1
            if count_operations_replenishment % 3 == 0:
                init_amaunt -= init_amaunt / 100 * 5
                print_account_amount(init_amaunt)
                return init_amaunt, count_operations_replenishment
        return init_amaunt, count_operations_replenishment

    else:  # снятие с процентами
        if init_amaunt - withdrawal_amount + (withdrawal_amount / 100 * 1.5) < 0:
            print('Снятие невозможно, сумма снятия превышает сумму на счете')
            print_account_amount(init_amaunt)
        else:
            init_amaunt -= withdrawal_amount + (withdrawal_amount / 100 * 1.5)
            print_account_amount(init_amaunt)
            count_operations_replenishment += 1
            if count_operations_replenishment % 3 == 0:
                init_amaunt -= init_amaunt / 100 * 5
                print_account_amount(init_amaunt)
                return init_amaunt, count_operations_replenishment
        return init_amaunt, count_operations_replenishment

def replenishment(init_amaunt, withdrawal_amount, count_operations_replenishment):
    init_amaunt += withdrawal_amount  # пополнение
    print_account_amount(init_amaunt)
    count_operations_replenishment += 1
    if count_operations_replenishment % 3 == 0:
        init_amaunt -= init_amaunt / 100 * 5
        print_account_amount(init_amaunt)
        return init_amaunt, count_operations_replenishment
    return init_amaunt, count_operations_replenishment


def menu(initial_amount, count_operations_replenishment):
    flag = True
    while flag:
        print_account_amount(initial_amount)  # печать суммы
        action = input('1 - пополнить\n2 - снять\n(любой знак) - выйти\n')
        if action == '1':
            flag_2 = True
            while flag_2:
                initial_amount = wealth_order(initial_amount)  # налог на богатство перед операцией
                replenishment_amount = int(input('Введите сумму пополнения кратную 50\n'))  # ввод суммы
                if multiplicity_check(replenishment_amount):  # проверка кратности
                    print('Сумма не кратная 50')
                    print_account_amount(initial_amount)
                else:
                    initial_amount, count_operations_replenishment = replenishment(initial_amount, replenishment_amount,
                                                                                   count_operations_replenishment)
                flag_2 = False

        elif action == '2':
            flag_2 = True
            while flag_2:
                initial_amount = wealth_order(initial_amount)  # налог на богатство перед операцией
                withdrawal_amount = int(input('Введите сумму снятия кратную 50\n'))
                if multiplicity_check(withdrawal_amount):  # проверка кратности
                    print('Сумма не кратная 50')
                    print_account_amount(initial_amount)
                else:
                    initial_amount, count_operations_replenishment = withdrawal(initial_amount, withdrawal_amount,
                                                                                count_operations_replenishment)
                flag_2 = False

        else:
            flag = False





if __name__ == '__main__':
    main()