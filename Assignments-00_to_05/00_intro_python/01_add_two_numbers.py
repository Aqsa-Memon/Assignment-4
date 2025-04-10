def add():
  print("This application for add two numbers")
  first_number = int(input("Enter your first number. "))
  second_number = int(input("Enter your second nunber. "))
  total = int(first_number + second_number)
  print(f'The total sum of {first_number} and {second_number} is = {total}')

if __name__ == "__main__":
  add()