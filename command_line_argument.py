import sys

# If you pass an argument in double quotes, python will take it as one argument

if len(sys.argv) < 2:
    sys.exit("Too few arguments...")  # exit by printing the given
elif len(sys.argv) > 2:
    sys.exit("Too many arguments...")

print(f"Hello, my name is {sys.argv[1]}.")

# for arg in sys.argv[1:]:
#     print("Hello, my name is", arg)

# try:
#     print(f"Hello, my name is {sys.argv[1]}.")
# except Exception as err:  # IndexError
#     print(err)
