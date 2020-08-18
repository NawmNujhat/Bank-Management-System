import random
import string
from luhn import *
global accounts
accounts=dict()


def luhn_algorithm(account):
    card=account

    temp=list(map(int,card))
    temp=temp[::-1]
    for i in range(len(temp)):

        if((i)%2==0):
            temp[i]=temp[i]*2
        if(temp[i]>9):
            temp[i]=temp[i]-9

    s=0
    c=0
    for i in range(len(temp)):
        s+=(temp[i])
    c=(s*9)%10
    return c

def create_account():

        iin = "400000"
        checksum = str(random.randint(0, 9))
        account_identifier = str(random.randint(100000000, 999999999))

        credit_card = ""
        credit=credit_card + iin + account_identifier
        credit_card = credit_card+credit + str(luhn_algorithm(credit))
        return(int(credit_card))


def create_pin():
    pin=str(random.randint(1000,9999))
    return pin
def log_account():
    print("\n")
    print("Enter your card number:")
    acid=int(input())
    print("Enter your PIN:")
    pid=input()
    if(accounts.get(acid) is not None):
         if(accounts[acid]==pid):
             while(True):
                print("\n")
                print("You have successfully logged in!")
                print("\n")
                print("1. Balance")
                print("2. Log out")
                print("0. Exit")
                a=int(input())
                if(a==1):
                    print("Balance: 0")
                elif(a==2):
                    print("You have successfully logged out!")
                    break;
                elif(a==0):
                    print("Bye!")
                    exit()
         else:
             print("\n")
             print("Wrong card number or PIN!")
    elif(accounts.get(acid) is None):
        print("Wrong card number or PIN!")
def main():
  i=0
  while(True):
      i=i+1
      if(i>1):
          print("\n")

      print("1. Create an account")
      print("2. Log into account")
      print("0. Exit")

      op=int(input())
      if(op==1):
          account=create_account()
          pin=create_pin()
          print("\n")
          print("Your card has been created\nYour card number:")
          print(account)
          print("Your card PIN:")
          print(pin)
          accounts[account]=pin
      elif(op==2):
          log_account()
      elif(op==0):
          print("Bye!")
          exit()


if __name__ == "__main__":
    main()