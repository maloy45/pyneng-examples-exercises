# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
list_ospf_route = ospf_route.split()
prot = list_ospf_route[0].replace('O', 'OSPF')
pre = list_ospf_route[1]
metr = list_ospf_route[2].strip('[]')
NHop = list_ospf_route[4].strip(',')
LUpd = list_ospf_route[5].strip(',')
OutInt = list_ospf_route[6]
print(f'''
Protocol:           {prot}
Prefix:             {pre}
AD/Metric:          {metr}
Next-Hop:           {NHop}
Last update:        {LUpd}
Outbound interface: {OutInt}
''')
