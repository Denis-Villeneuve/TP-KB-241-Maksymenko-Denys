from operations_oop import do_operation

def main():
    while True:
        do_operation()
        again = input("Do you want to continue? (y/n): ")
        if again.lower() != "y":
            break

if __name__ == "__main__":
    main()
