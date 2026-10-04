try:
    filename = input("Enter the file name: ")

    file = open(filename, "r")
    lines = file.readlines()

    item_count = 0
    free_items = 0
    amount = 0
    discount = 0

    for line in lines:
        line = line.strip()

        # Ignore blank lines
        if line == "":
            continue

        parts = line.split()

        # Discount line
        if parts[0] == "Discount":
            discount = int(parts[1])

        else:
            item_count += 1
            price = parts[1]

            # Free item
            if price == "Free":
                free_items += 1
            else:
                amount += int(price)

    final_amount = amount - discount

    print("No of items purchased:", item_count)
    print("No of free items:", free_items)
    print("Amount to pay:", amount)
    print("Discount given:", discount)
    print("Final amount paid:", final_amount)

    file.close()

except FileNotFoundError:
    print("File does not exist.")

except ValueError:
    print("Invalid data in the file.")

except IndexError:
    print("Invalid file format.")