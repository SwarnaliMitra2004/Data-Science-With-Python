#split()  → String → List
#join()   → List → String

def sort_colors(color_sequence: str) -> str:
    # Split the string by hyphens to create a list of individual colors
    colors_list = color_sequence.split('-')
    # Sort the list of colors alphabetically
    colors_list.sort()
    # Join the sorted list back into a single string with hyphens
    return '-'.join(colors_list)

colors =input("Enter colors : ")
print(sort_colors(colors))