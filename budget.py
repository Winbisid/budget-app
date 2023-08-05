# class Category:





# def create_spend_chart(categories):

class Category:
    def __init__(self, name):
        self.ledger = list()
        self.name = name
        self.amount = 0

    def deposit(self, amount, *args):
        self.amount += amount
        try:
            description = args[0]
        except:
            description = ''

        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, withdraw_amount, *args):
        try:
            description = args[0]
        except:
            description = ''

        if self.check_funds(withdraw_amount):
            self.ledger.append(
                {"amount": -withdraw_amount, 'description': description})
            self.amount -= withdraw_amount
            return True
        else:
            return False

    def get_balance(self):
        return self.amount

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.amount:
            return False
        else:
            return True

    def __str__(self):
        output = ''
        length_of_stars = int((30 - len(self.name))/2)
        stars = "*" * length_of_stars
        output += f"{stars}{self.name}{stars}\n"

        for item in self.ledger:
            desc = item['description']
            amount = str("%.2f" % item['amount'])
            if len(desc) > 23:
                desc = desc[:23]
            if len(amount) > 7:
                amount = amount[:7]

            desc_len = len(desc)
            amount_len = len(amount)

            space_len = 30 - (desc_len + amount_len)
            space = ' ' * space_len
            output += desc
            output += space
            output += amount + '\n'
        output += f"Total: {self.get_balance()}"
        return output

def create_spend_chart(categories):
    category_list = []
    spend_amount = []
    total_amount = 0
    percent_amount = []
    for category in categories:
        category_list.append(category.name)

        amount = 0
        for i in category.ledger:
            if i["amount"] < 0:

                amount += abs(i["amount"])
        spend_amount.append(amount)
        total_amount += amount
    for i in spend_amount:

        percent_amount= list(map(lambda amount: int((((amount / total_amount) * 10) // 1) * 10), spend_amount))
    Line = "Percentage spent by category\n"

    for value in reversed(range(0, 101, 10)):
        if value == 0:
            string = "  " + str(value) + "|"
        elif value < 100:
            string = " " + str(value) + "|"
        else:
            string = str(value) + "|"
        for i in percent_amount:
            if i >= value :
                string += " o "
            else:
                string += "   "

        Line += string + ' \n'

    dashLength = len(spend_amount) * 3 + 1
    Line += "    " + "-" * dashLength + '\n'

    longestStr = max(category_list, key=len)
    longestStrNum = len(longestStr)
    
    for value in range(0, longestStrNum):
        Line += "    "
        number = 1
        for category in category_list:
            
            if len(category) > value:

                Line += (" " + category[value] + " ")
                if number == len(category_list):
                    Line+=" "
                

            else:
                Line += "   "
              
            number+=1
        Line += "\n"
    Line = Line.rstrip()
    Line += "  "

    return Line