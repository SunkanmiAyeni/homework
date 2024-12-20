from enum import Enum
from decimal import Decimal

class Currency(Enum):
    TWENTY = "20.00", "Twenties"
    TEN    = "10.00", "Tens"
    FIVE   =  "5.00", "Fives"
    ONE    =  "1.00", "Ones"
    # more ...
    PENNY  =  "0.01", "Pennies"

    def __init__(self, denomination, print_name):
        self.denomination = Decimal(denomination)
        self.print_name = print_name

def change_return(cost, paid):
    cost = Decimal(cost)   
    paid = Decimal(paid)

    change = paid - cost
    change_dict = {}  # Before Python 3.6 dictionaries do not preserve order so a sorting may be needed before printing

    if change < 0:
       return None   # Better to raise an exception if performance is not a major concern

    # Better to do rounding here rather than before calculating the change
    # round() could also be used here, quantize() offers more rounding options, if needed
    precision = Decimal("0.01")
    change = change.quantize(precision)
    for cur in Currency:
        currency_cnt, change = divmod(change, cur.denomination)   
        if currency_cnt:  
            change_dict[cur] = currency_cnt
    return change_dict

if __name__ == "__main__":
    changes = change_return("30", "86.13")
    if changes is None:
       print('Insufficient funds')
    else:
       for cur, count in changes.items():
           print(f"{cur.print_name:<9}: {count}")