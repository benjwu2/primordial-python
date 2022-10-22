
todo_list = []

todo = input("Enter an item: ")

while todo != "":
    todo_list.append(todo)
    todo = input("Enter an item: ")

print("Your to do list:")
print("-" * len("Your to do list:"))
for items in todo_list:
    print(items)