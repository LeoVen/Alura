from datetime import date

class Contract:
    def __init__(self, date, customer, c_type):
        self.__date = date
        self.__customer = customer
        self.__c_type = c_type

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        self.__customer = customer

    @property
    def c_type(self):
        return self.__c_type

    @c_type.setter
    def c_type(self, c_type):
        self.__c_type = c_type

    def advance(self):
        if self.__c_type == 'NEW':
            self.__c_type = 'IN PROGRESS'
        elif self.__c_type == 'IN PROGRESS':
            self.__c_type = 'SUCCESSFUL'
        elif self.__c_type == 'SUCCESSFUL':
            self.__c_type = 'COMPLETED'

    def save_state(self):
        return State(Contract(  date = self.__date,
                                customer = self.__customer,
                                c_type = self.__c_type))
    
    def restore_state(self, state):
        self.__customer = state.contract.customer
        self.__date = state.contract.date
        self.__c_type = state.contract.c_type

class State:
    def __init__(self, contract):
        self.__contract = contract

    @property
    def contract(self):
        return self.__contract

class History:
    def __init__(self):
        self.__saved_states = []

    def get_state(self, index):
        return self.__saved_states[index]

    def set_state(self, state):
        self.__saved_states.append(state)

if __name__ == '__main__':

    hist = History()

    contract = Contract(date = date.today(), 
                        customer = 'John Walker',
                        c_type = 'NEW')

    print(contract.c_type)
    print(contract.customer)

    contract.advance()

    hist.set_state(contract.save_state())

    contract.advance()

    contract.customer = 'Hera Dolwort'
    hist.set_state(contract.save_state())

    contract.advance()

    hist.set_state(contract.save_state())

    print(contract.c_type)
    print(contract.customer)

    contract.restore_state(hist.get_state(0))

    print(contract.c_type)
    print(contract.customer)
