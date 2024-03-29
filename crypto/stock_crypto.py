import requests
import datetime

cryptos = {
    'bitcoin': 'Qwsogvtv82FCd',
    'etherum': 'razxDUgYGNAdQ',
    'dogecoin': 'a91GCGd_u96cF',
    'shibainu': 'xz24e0BjL',
    'litecoin': 'D7B1x_ks7WhV5',
}


def help_available_cryptos():
    """Informs user about avaible cryptos."""
    print("""bitcoin\netherum\ndogecoin\nshibainu\nlitecoin""")


def validate_crypto_name():
    crypto_name = str(input("enter the name of crypto which You want to choose: "))
    if crypto_name in cryptos:
        crypto_name = cryptos[crypto_name]
        return crypto_name, True
    else:
        print("Sorry we do not have that crypto")
        return None, False


def downloading_data(crypto_name):
    """Downloads from server chosen crypto data."""
    headers = {"x-access-token": "coinrankingd8901efc7e4b47aafe481b49cf5deed5d7dd3e8b27d1c6a1"}
    url = f"https://api.coinranking.com/v2/coin/{crypto_name}"
    r = requests.get(url, headers=headers)
    response = r.json()["data"]["coin"]
    chosen_crypto_symbol = response["symbol"]
    chosen_crypto_name = response["name"]
    chosen_crypto_price = response["price"]
    return response, chosen_crypto_price, chosen_crypto_name, chosen_crypto_symbol


def check_n_print_price(crypto_name):
    """Checks price of chosen crypto and appends that price to list to list"""
    response, chosen_crypto_price, chosen_crypto_name, chosen_crypto_symbol = downloading_data(crypto_name)
    print(f"Price of {chosen_crypto_name} is {float(chosen_crypto_price):.5f} [USD]")
    appending_sought_item_to_list(crypto_name)


def response_time_from_server():
    """Return time of function call out, function used for determine time of action in App.
    The time for is delivered as: [13.11.2021r. 12:09:05][day.month.year hour.minute.second]"""
    time_log = datetime.datetime.now().strftime("%d.%m.%Yr. %H:%M:%S")
    return time_log


def appending_sought_item_to_list(crypto_name):
    global price_list
    """Appends searched price of crypto to list as string."""
    response_time = response_time_from_server()
    response, chosen_crypto_price, chosen_crypto_name, chosen_crypto_symbol = downloading_data(crypto_name)
    item = f"[{response_time}] {chosen_crypto_symbol}: {chosen_crypto_name} {float(chosen_crypto_price):.5f} " \
           f"USD"
    price_list.append(item)



def single_crypto_data_log(crypto_name):
    """Appends or creates file crypto log.txt with history of checked prices, represented as every record in new line.
    Every line contains time:crypto symbol:crypto name:crypto price with 5 numbers after decimal."""
    response, chosen_crypto_price, chosen_crypto_name, chosen_crypto_symbol = downloading_data(crypto_name)
    with open("crypto log.txt", "a") as file:
        response_time = response_time_from_server()
        file.write(f"[{response_time}] {chosen_crypto_symbol}: {chosen_crypto_name} {float(chosen_crypto_price):.5f} "
                   f"USD\n ")


def sought_crypto_data_log():
    """Transfers elements from list to txt file, after transfer clears list."""
    with open("crypto log.txt", "a") as file:
        for item in price_list:
            file.write(item + "\n")
    price_list.clear()


def menu():
    """Creates menu for App, function that controls App."""
    action = input("""I want to: """)
    if action == "check price":
        crypto_name, returned_value = validate_crypto_name()
        if returned_value is True:
            check_n_print_price(crypto_name)
            menu()
        else:
            menu()
    elif action == "create log":
        crypto_name, returned_value = validate_crypto_name()
        if returned_value is True:
            single_crypto_data_log(crypto_name)
            print("\nFile with logs created/updated.\n")
            menu()
        else:
            menu()
    elif action == "save scores":
        crypto_name, returned_value = validate_crypto_name()
        if returned_value is True:
            sought_crypto_data_log()
            menu()
        else:
            menu()
    elif action == "exit":
        exit()
    elif action == "help":
        help_available_cryptos()
        menu()
    else:
        print("Unknown action.")
        menu()


price_list = []

if __name__ == '__main__':
    print("     Welcome to my CRYPTO App! :)"
          """what u want to do?")
        - check price of crypto type: check price
        - to check available cryptos type: help
        - create or append data of crypto price do file type: create log
        - save sought scores during running app and add to txt file, type: save scores
        - to exit app type: exit""")
    menu()
