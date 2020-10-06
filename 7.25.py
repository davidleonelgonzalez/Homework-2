# David Gonzalez
# 1630338

def exact_change(user_total):
    num_dollar = user_total // 100
    user_total %= 100
    num_quarter = user_total // 25
    user_total %= 25
    num_dime = user_total // 10
    user_total %= 10
    num_nickel = user_total // 5
    user_total %= 5
    num_penny = user_total
    return num_dollar, num_quarter, num_dime, num_nickel, num_penny


def main():
    input_val = int(input())
    num_dollar, num_quarter, num_dime, num_nickel, num_penny = exact_change(input_val)
    if input_val <= 0:
        print('no change')
    else:
        if num_dollar == 1:
            print('%d dollar' % num_dollar)
        elif num_dollar > 1:
            print('%d dollars' % num_dollar)

        if num_quarter == 1:
            print('%d quarter' % num_quarter)
        elif num_quarter > 1:
            print('%d quarters' % num_quarter)

        if num_dime == 1:
            print('%d dime' % num_dime)
        elif num_dime > 1:
            print('%d dimes' % num_dime)

        if num_nickel == 1:
            print('%d nickel' % num_nickel)
        elif num_nickel > 1:
            print('%d nickels' % num_nickel)

        if num_penny == 1:
            print('%d penny' % num_penny)
        elif num_penny > 1:
            print('%d pennies' % num_penny)


if __name__ == "__main__":
    main()