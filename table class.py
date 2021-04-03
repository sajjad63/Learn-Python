class Table(object):
    def __init__(hamoon, first_material, second_material, third_material):
        hamoon._top = first_material
        hamoon.stand = second_material
        hamoon.gaurd = third_material

    def show_table(hamoon):
        print("self:", hamoon)
        print("self:", hamoon.__dict__)
        print("self:", hamoon.__class__)
        print("self_getattribute_stand:", hamoon.__getattribute__("stand"))
        print("self._top:", hamoon._top)
        print("self.stand:", hamoon.stand)
        print("self.gaurd:", hamoon.gaurd)


wood_table = Table(first_material="wood", second_material="metal", third_material=False)
print("wood_table:", wood_table)
wood_table.show_table()
# Table.show_table(wood_table)