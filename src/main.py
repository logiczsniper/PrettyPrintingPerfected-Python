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

    def output(self, data):
        """
        Handles output based on self.return_string

        :param data: the data that will be either printed or returned.
        :type: str

        :return: if self.return_string is True, the data is returned.
        :rtype: str
        """

        if self.return_string:
            return data
        elif not self.return_string:
            print(data)

    def iterate_sequence(self, input_sequence):
        """
        Iterates through a sequence as its own method so that it can be recursive. Builds an output pattern to be used
        by other methods.

        :param input_sequence: the sequence to be iterated through.
        :type: list || tuple

        :return: the output string pattern to be used by other methods.
        :rtype: str
        """

        output = str()
        nested_dicts = list()

        for element in input_sequence:

            if type(element) == list or type(element) == tuple:
                if self.iterate_nested:
                    nested_list_output = self.iterate_sequence(element)
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
        """
        Iterates through a dict as its own method so that it can be recursive. Builds an output pattern to be used by
        other methods.

        :param input_dict: the dict to be iterated through.
        :type: dict

        :return: the output string pattern to be used by other methods.
        :rtype: str
        """

        output = str()
        nested_lists = list()

        for key, value in zip(input_dict.keys(), input_dict.values()):

            if type(value) == dict:
                if self.iterate_nested:
                    try:
                        output += self.prettify_dict(value, key)
                    except TypeError:
                        pass
                else:
                    continue
            elif type(value) == list or type(value) == tuple:
                try:
                    output += self.prettify_sequence(value, key)
                except TypeError:
                    pass
            else:
                if self.capitalize:
                    key = key if type(key) != str else key.capitalize()

                output += f"{key} -> {value}\n"

        if self.iterate_nested:
            for nested_list in nested_lists:
                nested_list_output = self.iterate_sequence(nested_list)
                output += "\n" + nested_list_output

        return output

    def prettify_sequence(self, input_sequence, output_title):
        """
        Uses self.iterate_through_list to prettify a list.

        :param input_sequence: the sequence to be prettified.
        :type: list || tuple

        :param output_title: the title that will be used for the output sequence.
        :type: str

        :return: if self.regular_print is True && self.return_string is True, return the pprint Printer output.
        :rtype: str
        """

        if not self.regular_print:

            iter_output = [self.iterate_sequence(input_sequence).split("\n")]

            for counter, element in enumerate(iter_output[0]):
                iter_output[0][counter] = element.format(counter + 1)

            full_output = "\n".join(iter_output[0])

            output_string = f"{output_title.capitalize()} \n{'_' * len(output_title)}\n\n" \
                            f"{full_output}"
            self.output(output_string)

        elif self.regular_print:

            if self.return_string:
                return self.pprint_printer.pformat(input_sequence)
            elif not self.return_string:
                self.pprint_printer.pprint(input_sequence)

    def prettify_dict(self, input_dict, output_title):
        """
        Uses self.iterate_through_dict to prettify a dict.

        :param input_dict: the dict to be prettified.
        :type: dict

        :param output_title: the title that will be used for the output dict.
        :type: str

        :return: if self.regular_print is True && self.return_string is True, return the pprint Printer output.
        :rtype: str
        """

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
        """
        Uses two methods above, recognises input data type, uses appropriate method.

        :param input_data: the data structure to be prettified.
        :type: list || dict || tuple

        :param output_title: the title that will be applied to the output.
        :type: str
        """

        if type(input_data) == list or type(input_data) == tuple:
            self.prettify_sequence(input_data, output_title)
        elif type(input_data) == dict:
            self.prettify_dict(input_data, output_title)
        else:
            self.output(input_data)

    @classmethod
    def classic_pretty_printer(cls):
        """ Provides a quick way to set up a pprint Printer. """

        return cls(True, True)
