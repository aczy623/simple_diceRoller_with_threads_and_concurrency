class Error(Exception):
    """base class for exeptions"""
    pass


class ZeroValueError(Error):
    """Raised when the entered value is a Zero"""
    pass


class NegativeValueError(Error):
    """Raised when a negative value is entered"""
pass

def DiceValues():
    go=True
    quantity=0
    diceType=0
    while go==True:
        try:
            quantity = int(input('enter the number of dice to roll: '))
            diceType = int(input('enter the type of dice you want to roll: '))
            go=False
        except ValueError:
            print('\nNot an integer, Please enter an integer\n')
        except ZeroValueError:
            print('\nZero is an invalid integer')
        except NegativeValueError:
            print('\nnegative numbers are invalid integers')

    new_Tuple= (quantity, diceType)
    return new_Tuple