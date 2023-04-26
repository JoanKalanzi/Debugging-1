

def get_most_common_letter(text):
    print(f"text ---> {text}")
    counter = {}
    for char in text:
        print(f" char in text {text}")
        counter[char] = counter.get(char, 0) + 1
        # get method --> the char is KEY and 0 is the default value and if the KEY  already exist then add + 1
        print(f"counter {counter}")

    """ letter = sorted(counter.items(), key=lambda item: item[1])
    print(f" sort the letters by value {letter}")
    """
    del counter[" "] 
    # this deletes the spaces in the list
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
    # lambda creates a new function
    print(f" letter after deleting space {letter}")
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")