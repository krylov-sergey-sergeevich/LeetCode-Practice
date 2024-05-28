def check(result, expected, message=""):
    if result != expected:
        print("ERROR: " + str(result) + " != " + str(expected) + " " + message)
    else:
        print("Success: " + str(result) + " == " + str(expected))
    print()
