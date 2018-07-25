from abc import ABC,abstractmethod


class InvalidBankException(Exception):

    def __init__(self,msg):
        super().__init__(msg)


class InvalidCustomerException(Exception) :

    def __init__(self,msg):
        super().__init__(msg)



class Bank(ABC):

    @abstractmethod
    def depositAmount(self,amount,atmpin):
        pass

    @abstractmethod
    def withdrawAmount(self,amount,atmpin):
        pass

    def checkIsValidCustomer(self,customer):
        if customer.bankType == 'SBI' or customer.bankType == 'HDFC' or customer.bankType == 'ICICI':
            return True
        else :
            raise InvalidCustomerException('You are not HDFC Customer but belongs to ' + customer.bankType)


class HDFC (Bank) :
    hdfcBalance = 100000
    listofPins = ['1234','4567','8910']

    def __init__(self,customer):
        #isValidCustomer = super(HDFC, self).__init__(self.checkIsValidCustomer(customer))
        isValidCustomer = self.checkIsValidCustomer(customer)
        if isValidCustomer and HDFC.listofPins.__contains__(customer.pin) :
            customer.HDFCValidCustomer = True
        else :
            customer.HDFCValidCustomer = False

    def depositAmount(self,customer,depositAmnt):
        if customer.HDFCValidCustomer :
            HDFC.hdfcBalance += depositAmnt
            customer.balance += depositAmnt
        else :
            raise InvalidBankException('You are not HDFC Customer but belongs to '+customer.bankType)

    def withdrawAmount(self,customer,withDrawAmnt):
        if customer.HDFCValidCustomer :
            HDFC.hdfcBalance -= withDrawAmnt
            customer.balance -= withDrawAmnt

class Customer:

    def __init__(self,amnt,btype,atmpin):
        self.balance = amnt
        self.bankType = btype
        self.pin= atmpin

    def __str__(self):
        return 'Customer Balance :{}\n' \
               'Customer Balance :{}\n' \
               'Customer Balance : {}\n'.format(self.balance,self.bankType,self.pin)


cust = Customer(12000,'HDFC','1214')
print('Before1 -- ',cust)

hdfcBank = HDFC(cust)
print('Before2 -- ',cust)

hdfcBank.withdrawAmount(cust,1000)
print(HDFC.hdfcBalance)
print('Before3 -- ',cust)