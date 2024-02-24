import json

my_file = open("sample-data.json", "r")
x = json.load(my_file)
print("Interface Status")
print(
    "================================================================================"
)
print(
    "DN                                                 Description           Speed    MTU"
)
print("-------------------------------------------------- --------------------  ------  ------")

a=x['imdata']
def printing_dn(n):
    print(n['dn'], end="                             ")
    print(n['descr'], end=" ")
    print(n['speed'], end="   ")
    print(n['mtu'])
for item in a:
    b=item['l1PhysIf']
    c=b['attributes']
    if c['dn']=="topology/pod-1/node-201/sys/phys-[eth1/33]":
        printing_dn(c)
    if c['dn']=="topology/pod-1/node-201/sys/phys-[eth1/34]":
        printing_dn(c)
    if c['dn']=="topology/pod-1/node-201/sys/phys-[eth1/35]":
        printing_dn(c)