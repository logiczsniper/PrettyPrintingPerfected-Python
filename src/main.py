import pprint


class PrettyPrinter:

    def __init__(self, regular_print=False, return_string=False, iterate_nested=True, capitalize=True, indent=1):

        self.regular_print = regular_print
        self.return_string = return_string
        self.iterate_nested = iterate_nested
        self.capitalize = capitalize

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

    # TODO: build functions that iterate through the entire data structure, returning a list of lists found and a list
    # TODO: dicts found
    # TODO: take output from above method, combine the data structures into one big list/ one big dict. Use these.

    def get_nested_structures(self, input_data):

        all_lists = list()
        all_dicts = list()

        for element in input_data:

            if type(element) == list:
                all_lists.append(element)
                output = self.get_nested_structures(element)
                all_lists.extend(output)

            elif type(element) == dict:
                all_lists.append(element)
                output = self.get_nested_structures(element)
                all_dicts.extend(output)

        return [all_lists, all_dicts]

    def iterate_through_list(self, input_list):

        output = str()
        nested_dicts = list()

        for element in input_list:

            if type(element) == list:
                if self.iterate_nested:
                    nested_list_output = self.iterate_through_list(element)
                    output += nested_list_output
                else:
                    continue
            elif type(element) == dict:
                nested_dicts.append(element)
                continue
            else:
                if self.capitalize:
                    element = element if type(element) != str else element.capitalize()

                output += "{})" + f" {element}\n"

        if self.iterate_nested:
            for nested_dict in nested_dicts:
                nested_dict_output = self.iterate_through_dict(nested_dict)
                output += "\n" + nested_dict_output

        return output

    def iterate_through_dict(self, input_dict):

        output = str()
        nested_lists = list()

        for key, value in zip(input_dict.keys(), input_dict.values()):

            if type(value) == dict:
                if self.iterate_nested:
                    nested_dict_output = self.iterate_through_dict(value)
                    output += nested_dict_output
                else:
                    continue
            elif type(value) == list:
                nested_lists.append(value)
                continue
            else:
                if self.capitalize:
                    key = key if type(key) != str else key.capitalize()

                output += f"{key} -> {value}\n"

        if self.iterate_nested:
            for nested_list in nested_lists:
                nested_list_output = self.iterate_through_list(nested_list)
                output += "\n" + nested_list_output

        return output

    def prettify_list(self, input_list, output_title):

        if not self.regular_print:

            iter_output = [self.iterate_through_list(input_list).split("\n")]

            for counter, element in enumerate(iter_output[0]):
                iter_output[0][counter] = element.format(counter + 1)

            full_output = "\n".join(iter_output[0])

            output_string = f"{output_title.capitalize()} \n{'_' * len(output_title)}\n\n" \
                            f"{full_output}"
            self.output(output_string)

        elif self.regular_print:

            if self.return_string:
                return self.pprint_printer.pformat(input_list)
            elif not self.return_string:
                self.pprint_printer.pprint(input_list)

    def prettify_dict(self, input_dict, output_title):

        if not self.regular_print:

            output_string = f"{output_title.capitalize()} \n{'_' * len(output_title)}\n\n" \
                            f"{self.iterate_through_dict(input_dict)}"
            self.output(output_string)

        elif self.regular_print:

            if self.return_string:
                return self.pprint_printer.pformat(input_dict)
            elif not self.return_string:
                self.pprint_printer.pprint(input_dict)

    def peachy_print(self, input_data, output_title):

        print(self.get_nested_structures(input_data))

        if type(input_data) == list:
            self.prettify_list(input_data, output_title)
        elif type(input_data) == dict:
            self.prettify_dict(input_data, output_title)
        else:
            self.output(input_data)
