import random
import string
import sqlite3
from sqlite3 import Error

global accounts




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

def do_transfer(acid,receiver,amount):
    cur.execute("SELECT balance FROM card WHERE number=?", (acid,))
    donor=cur.fetchall()
    cur.execute("SELECT balance FROM card WHERE number=?", (receiver,))
    receiverr = cur.fetchall()
    if(acid==receiver):
        print(" “You can't transfer money to the same account!”")
    elif(donor[0][0]<amount):
        print("Not enough money!")
    else:
        balance_donor=donor[0][0]-amount
        balance_receiver=receiverr[0][0]+amount
        cur.execute("UPDATE card SET balance=? WHERE number=?", (balance_donor, acid))
        cur.execute("UPDATE card SET balance=? WHERE number=?", (balance_receiver, receiver))
        conn.commit()
        print("Success!")





def log_account():
    print("\n")
    print("Enter your card number:")
    acid=input()
    print("Enter your PIN:")
    pid=input()
    i=0

    cur.execute("SELECT * FROM card WHERE number=? And pin=?", (acid, pid))
    row=cur.fetchall()
    if(len(row)==0):
        print("\n")
        print("Wrong card number or PIN!")
    else:
        while (True):
            i=i+1
            if(i==1):
                print("\n")
                print("You have successfully logged in!")
            print("\n")
            print("1. Balance")
            print("2. Add income")
            print("3. Do transfer")
            print("4. Close account")
            print("5. Log out")

            print("0. Exit")

            a = int(input())
            if (a == 1):
                cur.execute("SELECT balance FROM card WHERE number=? And pin=?", (acid, pid))
                row = cur.fetchall()
                print("Balance: ",row[0][0])
            elif(a==2):
                print("\n")
                print("Enter income:")
                income=int(input())
                cur.execute("SELECT balance FROM card WHERE number=? And pin=?", (acid, pid))
                row = cur.fetchall()
                balance=row[0][0]+income
                cur.execute("UPDATE card SET balance=? WHERE number=?",(balance,acid))
                conn.commit()
                print("Income was added!")
            elif(a==3):
                print("Transfer")
                print("Enter card number:")
                transfer = input()
                list_transfer=transfer[:-1]
                if(transfer[0]!='4'):
                    print("Such a card does not exist.")
                elif(transfer[len(transfer)-1]!=str(luhn_algorithm(list_transfer) )and transfer[0]=='4'):
                    print("Probably you made mistake in the card number. Please try again!")

                elif(transfer[len(transfer)-1]==str(luhn_algorithm(list_transfer)) and transfer[0]=='4'):

                  cur.execute("SELECT * FROM card WHERE number=?", (transfer,))
                  row_transfer=cur.fetchall()
                  print(row_transfer)
                  if(len(row_transfer)==0):
                     print("Such a card does not exist.")
                  else:
                     print("Enter how much money you want to transfer:")
                     amount=int(input())
                     print(amount)
                     do_transfer(acid,transfer,amount)
            elif(a==4):
                print("\n")
                print("The account has been closed!")
                cur.execute("Delete From card where number= ?",(acid,))
                conn.commit()
            elif (a == 5):
                print("You have successfully logged out!")
                break
            elif (a == 0):
                print("Bye!")
                exit()


def main():
  global conn,cur
  conn = sqlite3.connect('card.s3db')
  cur=conn.cursor()
  createTable="Create Table IF NOT EXISTS card(id integer primary key autoincrement,number text,pin text,balance INTEGER DEFAULT 0)"
  cur.execute(createTable)
  conn.commit()
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
          account_number=create_account()
          PIN=create_pin()
          print("\n")
          print("Your card has been created\nYour card number:")
          print(account_number)
          account_number=str(account_number)
          print("Your card PIN:")
          print(PIN)
          account_number=str(account_number)
          cur.execute("INSERT INTO card (id,number, pin,balance) VALUES ((SELECT MAX(id) + 1 FROM card), ?, ?, ?)", (account_number, PIN,0))

          conn.commit()


      elif(op==2):
          log_account()
      elif(op==0):
          print("Bye!")
          exit()


if __name__ == "__main__":
    main()
