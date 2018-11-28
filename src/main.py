from pprint import PrettyPrinter


class PeachyPrinter:

    def __init__(self, regular_print=False, return_string=False, iterate_nested=True, capitalize=True, indent=1):
        """
        Set up printer with provided printing defaults.

        :param regular_print: if True, the pprint printer is used.
        :type: bool

        :param return_string: if True, the printer will return the string rather than print it.
        :type: bool

        :param iterate_nested: if False, the printer will completely ignore nested data structures.
        :type: bool

        :param capitalize: if False, elements will NOT be capitalized.
        :type: bool

        :param indent: set the indent of the built in pprint Pretty Printer.
        :type: int
        """

        self.regular_print = regular_print
        self.return_string = return_string
        self.iterate_nested = iterate_nested
        self.capitalize = capitalize
        self.pprint_printer = PrettyPrinter(indent=indent)
        self.current_data_type = None
        self.single_output = str()

    def output(self):
        """
        Handles output based on self.return_string

        :return: if self.return_string is True, the data is returned.
        :rtype: str
        """

        data = self.single_output.strip()

        if self.return_string:
            return data
        elif not self.return_string:
            print(data)

    def iterate_sequence(self, input_sequence):
        """
        Iterates through a sequence as its own method so that it can be recursive. Builds an output pattern to be used
        by other methods.

        :param input_sequence: the sequence to be iterated through.
        :type: list || tuple || set

        :return: the output string pattern to be used by other methods.
        :rtype: str
        """

        output = str()
        nested_dicts = list()
        nested_sets = list()
        nested_tuples = list()

        for element in input_sequence:

            if type(element) in [list, tuple]:
                if type(input_sequence) == set:
                    nested_tuples.append(element)
                    continue
                elif self.iterate_nested:
                    nested_list_output = self.iterate_sequence(element)
                    if not isinstance(element, self.current_data_type):
                        # output += '\n'
                        pass
                    output += f'{nested_list_output}'
                else:
                    continue
            elif type(element) == dict:
                nested_dicts.append(element)
                continue
            elif type(element) == set:
                nested_sets.append(element)
                continue
            else:
                if self.capitalize:
                    element = element if type(element) != str else element.capitalize()
                if type(input_sequence) == set:
                    output += "-" + f" {element}\n"
                else:
                    output += "{})" + f" {element}\n"

        if self.iterate_nested:

            for nested_dict in nested_dicts:

                output += "\n" + self.iterate_dict(nested_dict)

            for nested_set in nested_sets:

                output += self.iterate_sequence(nested_set)

            for nested_tuple in nested_tuples:

                output += self.iterate_sequence(set(nested_tuple))

        return output

    def iterate_dict(self, input_dict):
        """
        Iterates through a dict as its own method so that it can be recursive. Builds an output pattern to be used by
        other methods.

        :param input_dict: the dict to be iterated through.
        :type: dict

        :return: the output string pattern to be used by other methods.
        :rtype: str
        """

        output = str()
        nested_lists = dict()
        nested_sets = dict()

        for key, value in zip(input_dict.keys(), input_dict.values()):

            if type(value) == dict:
                if self.iterate_nested:
                    try:
                        output += self.prettify_dict(value, key)
                    except TypeError:
                        pass
                else:
                    continue
            elif type(value) in [list, tuple]:
                nested_lists[key] = value
            elif type(value) == set:
                nested_sets[key] = value
            else:
                if self.capitalize:
                    key = key if type(key) != str else key.capitalize()
                output += f"{key} -> {value}\n"

        if self.iterate_nested:

            for nested_list_name, nested_list in zip(nested_lists.keys(), nested_lists.values()):

                output += "\n"
                self.prettify_sequence(nested_list, nested_list_name)

            for nested_set_name, nested_set in zip(nested_sets.keys(), nested_sets.values()):

                output += "\n"
                self.prettify_sequence(nested_set, nested_set_name)

        return output

    def prettify_sequence(self, input_sequence, output_title):
        """
        Uses self.iterate_through_list to prettify a list.

        :param input_sequence: the sequence to be prettified.
        :type: list || tuple || set

        :param output_title: the title that will be used for the output sequence.
        :type: str

        :return: if self.regular_print is True && self.return_string is True, return the pprint Printer output.
        :rtype: str
        """

        if not self.regular_print:
            if type(input_sequence) != set:
                iter_output = [self.iterate_sequence(input_sequence).split("\n")]

                for counter, element in enumerate(iter_output[0]):

                    iter_output[0][counter] = element.format(counter + 1)

                full_output = "\n".join(iter_output[0])

            else:

                full_output = self.iterate_sequence(input_sequence)

            output_title = str(output_title)
            output_string = f"{output_title.title()}\n{'_' * len(output_title)}\n\n" \
                            f"{full_output}"
            self.single_output += f'\n{output_string}'
        elif self.regular_print:
            if self.return_string:
                return self.pprint_printer.pformat(input_sequence)
            elif not self.return_string:
                self.pprint_printer.pprint(input_sequence)

    def prettify_dict(self, input_dict, output_title):
        """
        Uses self.iterate_dict to prettify a dict.

        :param input_dict: the dict to be prettified.
        :type: dict

        :param output_title: the title that will be used for the output dict.
        :type: str

        :return: if self.regular_print is True && self.return_string is True, return the pprint Printer output.
        :rtype: str
        """

        if not self.regular_print:
            output_string = f"{output_title.title()}\n{'_' * len(output_title)}\n\n" \
                            f"{self.iterate_dict(input_dict)}"
            self.single_output += f'\n{output_string}'
        elif self.regular_print:
            if self.return_string:
                return self.pprint_printer.pformat(input_dict)
            elif not self.return_string:
                self.pprint_printer.pprint(input_dict)

    def peachy_print(self, input_data, output_title):
        """
        Uses two methods above, recognises input data type, uses appropriate method.

        :param input_data: the data structure to be prettified.
        :type: list || dict || tuple || set

        :param output_title: the title that will be applied to the output.
        :type: str
        """

        self.current_data_type = type(input_data)
        self.single_output = str()
        if self.current_data_type in [list, tuple, set]:
            self.prettify_sequence(input_data, output_title)
        elif self.current_data_type == dict:
            self.prettify_dict(input_data, output_title)
        else:
            return str(input_data)
        return self.output()

    @classmethod
    def classic_pretty_printer(cls):
        """ Provides a quick way to set up a pprint Printer. """

        return cls(True, True)
