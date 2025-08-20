import os

def greet_user(name):
    print(f"Hello, {name}!")

def calculate():
    expr = input("Enter a math expression: ")
    print("Result:", eval(expr))

def list_dir():
    folder = input("Enter folder path: ")
    os.system(f"dir {folder}") 

if __name__ == "__main__":
    greet_user("Zero")
    calculate()
    list_dir()

