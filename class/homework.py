from datetime import date
class Company():
    def __init__(self, name, year, product):
        self.name = name
        self.year = year
        self.product = product

    @classmethod
    def start_comp(cls, name, year,  product):
        return cls(name, date.today().year-year, product)

    def sroc_tele(self):
        if garantee >= 3:
            return f"У этого телефона истекла горантия"
        if garantee < 3:
            return f"У этого телефона не истекла горантия"
    def display(self):
        return f"NAME_OF_COMPANY: {self.name}" \
               f" AGE_OF_COMPANY: {self.year}" \
               f"  PRODUCT: {self.product}"

company = Company("Xiaomi", 5, "POCO")
print(company.start_comp("Xiaomi", 2018, "POCO").display())
garantee = int(input(f"Сколько лет назад вы купили:"))
print(company.sroc_tele())

