from src.main import PrettyPrinter

if __name__ == '__main__':
    prettyPrinter = PrettyPrinter()
    user_data = ['apples', 'belvita bars', ['hello_one', 'hello_two', 'hello_three'],
                 {'id': '8472883', 'name': 'UserName', 'password': 'Password'}, 'milk (organic)',
                 ['hello_four', ['hello_five']],
                 'twinkies', 'yogurt']

    output = prettyPrinter.peachy_print(user_data, 'User Data')
