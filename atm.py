import random
class ATM:
  def __init__(self, username, password, balance):
    self.username = username
    self.password = password
    self.balance = balance
  def check_credentials(self, username, password):
    return self.username == username and self.password == password
  def withdraw(self):
    amount = int(input("Enter amount to withdraw: "))
    if amount <= self.balance:
      self.balance -= amount
      print(f"Withdrawal successful. New balance is {self.balance}.")
    else:
      print("Insufficient funds.")
  def deposit(self):
    amount = int(input("Enter amount to deposit: "))
    self.balance += amount
    print(f"Deposit successful. New balance is {self.balance}.")
  def get_balance(self):
    print(f"Current balance is {self.balance}.")
  def generate_otp(self):
    otp = random.randint(100000, 999999)
    print(f"Your OTP is {otp}.")
    return otp
user1 = ATM("Dharshini","cric123", 5000)
username = input("Enter your username: ")
password = input("Enter your password: ")
otp=user1.generate_otp()
print("Enter your otp :")
n=int(input())
if(n==otp):
 print("Enter your choice 1.Deposit 2.Withdraw 3.Get Balance")
 choice=int(input())
 if(choice==1):
  user1.deposit()
 elif(choice==2):
  user1.withdraw()
 elif(choice==3):
  user1.get_balance()
 else:
  print("Wrong Choice")
else:
 print("Wrong OTP Please try again ")
