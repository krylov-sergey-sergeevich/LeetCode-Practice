def check(a, b, message=""):
    if a != b:
        print("ERROR: " + str(a) + " != " + str(b) + " " + message)
    else:
        print("Success: " + str(a) + " == " + str(b))
    print()
