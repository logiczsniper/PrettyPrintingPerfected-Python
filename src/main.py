import pprint


class PrettyPrinter:

    def __init__(self, regular_print=False, return_string=False, iterate_nested=True, indent=1):

        self.regular_print = regular_print
        self.return_string = return_string
        self.iterate_nested = iterate_nested

        self.pprint_printer = pprint.PrettyPrinter(indent=indent)

    def update_regular_print_status(self, new_status):

        assert type(new_status) == bool
        self.regular_print = new_status

    def update_return_string_status(self, new_status):

        assert type(new_status) == bool
        self.return_string = new_status

    def update_pprinter_indent(self, new_indent):

        assert type(new_indent) == int
        self.pprint_printer._indent_per_level = new_indent

    @classmethod
    def classic_pretty_printer(cls):

        return cls(True, True)

    def output(self, data):

        if self.return_string:
            return data
        elif not self.return_string:
            print(data)

    def iterate_through_list(self, input_list):

        output = str()

        for element in input_list:

            if type(element) == list:
                if self.iterate_nested:
                    nested_list_output = self.iterate_through_list(element)
                    output += nested_list_output
                else:
                    continue
            else:
                element = element if type(element) != str else element.capitalize()
                output += "{})" + f" {element}\n"

        return output

    def prettify_list(self, input_list, output_title):

        if not self.regular_print:

            iter_output = [self.iterate_through_list(input_list).split("\n")]

            for counter, element in enumerate(iter_output[0]):
                iter_output[0][counter] = element.format(counter+1)

            full_output = "\n".join(iter_output[0])

            output_string = f"{output_title.capitalize()} \n{'_' * len(output_title)}\n\n" \
                            f"{full_output}"
            self.output(output_string)

        elif self.regular_print:

            if self.return_string:
                return self.pprint_printer.pformat(input_list)
            elif not self.return_string:
                self.pprint_printer.pprint(input_list)
