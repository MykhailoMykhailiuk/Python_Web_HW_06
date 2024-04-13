from prettytable import PrettyTable


def table(field_names, data):
    
    table = PrettyTable()
    table.field_names = field_names
    for i in data: 
        table.add_row(i)
    return table