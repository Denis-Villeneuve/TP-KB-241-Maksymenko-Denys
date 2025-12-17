from operations import do_operation
import logging

logging.basicConfig(
    filename="calc.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def main():
    while True:
        do_operation()
        again = input("Do you want to continue? (y/n): ")
        if again.lower() != "y":
            break

if __name__ == "__main__":
    main()
