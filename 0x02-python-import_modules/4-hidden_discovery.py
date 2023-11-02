#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    # The code imports a module called hidden_4.pyc already compiled
    # The dir function returns all attributes of the object and stores in var
    # The for loop checks the if anyone starts with two underscore and skips
    # Then prints the variable that the loop uses to store them

    contents = dir(hidden_4)
    for name in contents:
        if name[:2] != "__":
            print(name)
