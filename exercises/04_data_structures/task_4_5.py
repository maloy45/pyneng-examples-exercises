# -*- coding: utf-8 -*-
'''
Задание 4.5

Из строк command1 и command2 получить список VLANов,
которые есть и в команде command1 и в команде command2.

Результатом должен быть список: ['1', '3', '8']

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

command1_vlans_mn = set(command1[command1.find('1')::].split(','))
command2_vlans_mn = set(command2[command2.find('1')::].split(','))
peresechenie = list(command1_vlans_mn.intersection(command2_vlans_mn))
peresechenie.sort()
print(peresechenie)
