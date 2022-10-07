#I wanted to try a technique to invert the array and delete the top.
main_list = []
main_list.append("apple")
main_list.append("apricot")
main_list.append("banana")
main_list.append("cherry")
main_list.append("tomato")

print('---------------------------------')
print(main_list)
print('---------------------------------')

new_fruit = input("What fruits do you like?")
main_list.append(new_fruit)

print('---------------------------------')
print("New fruit is added")
print(main_list)
print('---------------------------------')

#Main subject below

main_list.reverse()
del main_list[0]
print("the latest stuff"+new_fruit+"were eliminated")
print(main_list)

