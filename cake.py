wight = int(input())
length = int(input())
available_pieces = wight * length
ordered_pieces = 0
pieces_counter = 0
extra_pieces = 0
species_to_give = True

while available_pieces > 0:
    order = input()
    if order == "STOP":
        break
    else:
        ordered_pieces = int(order)
    available_pieces -= ordered_pieces
    pieces_counter += ordered_pieces
else:
    extra_pieces = abs(available_pieces)
    species_to_give = False

if species_to_give:
    print(f"{available_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {extra_pieces} pieces more.")
