filename="settings.dat"
with open(filename, "wb") as f:
    f.write(b"Working with files")

my_file = open(filename, "wb")
user_input = input("enter your name:")
try:
    my_file.write(user_input('utf8'))
except Exception as e:
    import traceback
    traceback.print_exc()
    raise
    print("not shown")
finally:
    my_file.close()
    print("OK, all done")


with open(filename, "rb") as f_in:
    print(f_in.read().decode('utf8'))

