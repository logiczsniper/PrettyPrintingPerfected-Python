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
        self.logo = """
__                     .__        __   
'--`      _____________|__| _____/  |_
 _|,--.   \____ \_  __ \  |/    \   __\\
/ `)   \  |  |_> >  | \/  |   |  \  |  
\      |  |   __/|__|  |__|___|  /__|  
 '.___/   |__|                 \/     
 
    ¬Logan Czernel
        """

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
        nested_dicts, nested_sets, nested_tuples = list(), list(), list()

        for element in input_sequence:

            element_type = type(element)

            if element_type in [list, tuple]:
                if type(input_sequence) == set:
                    nested_tuples.append(element)
                    continue
                elif self.iterate_nested:
                    nested_list_output = self.iterate_sequence(element)
                    output += f'{nested_list_output}'
            elif element_type == dict:
                nested_dicts.append(element)
            elif element_type == set:
                nested_sets.append(element)
            else:
                if self.capitalize:
                    element = element if element_type != str else element.capitalize()
                if type(input_sequence) == set:
                    output += "-" + f" {element}\n"
                else:
                    output += "{})" + f" {element}\n"

        if self.iterate_nested:

            for nested_structures in [nested_dicts, nested_sets, nested_tuples]:

                for data_structure in nested_structures:

                    if type(data_structure) == dict:
                        output += "\n" + self.iterate_dict(data_structure)
                    elif type(data_structure) == set:
                        output += self.iterate_sequence(data_structure)
                    else:
                        output += self.iterate_sequence(set(data_structure))

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
        nested_sequences = dict()

        for key, value in zip(input_dict.keys(), input_dict.values()):

            value_type = type(value)

            if value_type == dict:
                if self.iterate_nested:
                    try:
                        output += self.prettify_dict(value, key)
                    except TypeError:
                        pass
            elif value_type in [list, tuple]:
                nested_sequences[key] = value
            elif value_type == set:
                nested_sequences[key] = value
            else:
                if self.capitalize:
                    key = key if type(key) != str else key.capitalize()
                output += f"{key} -> {value}\n"

        if self.iterate_nested:

            for nested_sequence_name, nested_sequence in zip(nested_sequences.keys(), nested_sequences.values()):

                output += "\n"
                self.prettify_sequence(nested_sequence, nested_sequence_name)

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
            if self.current_data_type != set:
                iter_output = self.iterate_sequence(input_sequence)
                full_output = iter_output.format(*[i+1 for i in range(iter_output.count("{}"))])
            else:
                full_output = self.iterate_sequence(input_sequence)
            output_title = str(output_title)
            output_string = f"{output_title.title()}\n{'_' * len(output_title)}\n\n{full_output}"
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
            output_string = f"{output_title.title()}\n{'_' * len(output_title)}\n\n{self.iterate_dict(input_dict)}"
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
