short_tuple = "A", "B" # tuple without brackets
a_bit_clearer_tuple = ("A", "B") # tuple with brackets
tuple_within_list = [("A", "B")] # tuple in a list

# cant add or remove to a tuple using append or remove methods
short_tuple = short_tuple + ("C",) # add to a tuple
print(short_tuple)