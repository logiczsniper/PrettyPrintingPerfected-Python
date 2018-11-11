from src.main import PrettyPrinter

if __name__ == '__main__':
    prettyPrinter = PrettyPrinter.classic_pretty_printer()
    prettyPrinter.update_pprinter_indent(4)
    groceriesList = ['apples', 'belvita bars', ['hello_one', 'hello_two', 'hello_three'],
                     'donuts', 'milk (organic)', ['hello_four', ['hello_five']],
                     'twinkies', 'yogurt']

    output = prettyPrinter.prettify_list(groceriesList, 'groceries list')
    print(output)
