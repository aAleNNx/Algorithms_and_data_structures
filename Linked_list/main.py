from Linked_list import linked_list
from doubly_linked_list import doubly_linked_list


lst = [('AGH', 'Kraków', 1919),
('UJ', 'Kraków', 1364),
('PW', 'Warszawa', 1915),
('UW', 'Warszawa', 1915),
('UP', 'Poznań', 1919),
('PG', 'Gdańsk', 1945)]

uczelnie = doubly_linked_list()
for i in range(3):
    uczelnie.append(lst[i])
for i in range(3, len(lst)):
    uczelnie.add(lst[i])
uczelnie.print_list()

print(uczelnie.length())

uczelnie.remove()
print(uczelnie.get())

uczelnie.remove_end()
uczelnie.print_list()
uczelnie.print_back()

uczelnie.destroy()
print(uczelnie.is_empty())
uczelnie.remove()
uczelnie.remove_end()
uczelnie.append(lst[0])
uczelnie.remove_end()
print(uczelnie.is_empty())
