import logging
import logging.config
import json
from enum import Enum

from typing import (
    List,
    Dict,
)
shopping_list: List = list()
last_price: List = list()
lowest_list_price: List = list()
you_bought: List = []


class User:
    """ create account for user """
    def __init__(self, new_username, last_name,
                 new_email, new_password, phone):
        self.new_username = new_username
        self.last_name = last_name
        self.new_email = new_email
        self.new_password = new_password
        self.phone = phone

    @property
    def new_username(self):
        """ getter for private new_username """
        return self.__new_username

    @new_username.setter
    def new_username(self, change_name):
        """

        Parameters
        ----------
        change_name :comparison attributable
            

        Returns condition --> true or false
        -------

        """

        if not change_name[0].isalpha():
            raise ValueError("your name should start with str")
        self.__new_username = change_name

    @property
    def last_name(self):
        """ """
        return self.__last_name

    @last_name.setter
    def last_name(self, change_last_name):
        """

        Parameters
        ----------
        change_last_name :comparison attributable
            

        Returns true or false
        -------

        """

        if not change_last_name[0].isalpha():
            raise ValueError("your last name should start with str")
        self.__last_name = change_last_name

    @property
    def new_email(self):
        """ """
        return self.__new_email

    @new_email.setter
    def new_email(self, change_email):
        """

        Parameters
        ----------
        change_email : comparison attributable
            

        Returns true or false
        -------

        """

        if "@gmail.com" not in change_email:
            raise ValueError("your email should have @gmail.com")
        self.__new_email = change_email

    @property
    def new_password(self):
        """ """
        return self.__new_password

    @new_password.setter
    def new_password(self, change_password):
        """

        Parameters
        ----------
        change_password : comparison attributable
            

        Returns true or false
        -------

        """

        if len(change_password) <= 6:
            raise ValueError("your password should more than 6 number")
        if not change_password.isalpha:
            raise ValueError("you should use character in your password")
        self.__new_password = change_password

    @property
    def phone(self):
        """ """
        return self.__phone

    @phone.setter
    def phone(self, change_phone):
        """

        Parameters
        ----------
        change_phone : comparison attributable
            

        Returns true or false
        -------

        """

        if not len(change_phone) == 11:
            raise ValueError("your phone should have 11 number")
        self.__phone = change_phone

class Create_account(User):
    """ create account and use inheritance """
    def __init__(self):
        super().__init__(new_username, last_name,
                         new_email, new_password, phone)
        with open('C:/just for ehsan/python/new/in_home/shopping_list/oop/login_users_oop.json', mode='r') as file:
            users_database = json.load(file)
            users_database[self.new_email] = {
                'password': self.new_password,
                'first': self.new_username,
                'last': self.last_name,
                'phone': self.phone
                }
            with open('C:/just for ehsan/python/new/in_home/shopping_list/oop/login_users_oop.json', mode='w') as f:
                json.dump(users_database, f, indent=4, separators=(', ', ': '))



    def check_logging(email_login, password_login):
        """

        Parameters
        ---------- 
        email_login : your last email that you created before
            
        password_login : your last password that you created before
            

        Returns true or false  for your login
        -------

        """
        with open('C:/just for ehsan/python/new/in_home/shopping_list/oop/login_users_oop.json', mode='r') as file:
            register = json.load(file)
            
            if email_login in register:
                if password_login == register[email]['password']:
                    print("welcome to our shopping")
                else:
                    print("your email or password is incorrect")
                    print("if you forgot your password or email write : yes\
if no write no")
            else:
                print("your email or password is incorrect")
                print("if you forgot your password or email write : yes\
if no write no")

    def back_password(email_b, name_b, last_name_b, phone_b):
        """

        Parameters
        ----------
        email_b : your last email that created by your self

        name_b : your last name that created by your self

        last_name_b : your last name that created by your self

        phone_b : your phone that created by your self

        Returns your last password that you forgot 
-------

        """
        with open('./login_users_oop', mode='r') as file:
            back_register = json.load(file)
            if email in back_register:
                if name_b == back_register[email]['first']:
                    if last_name_b == back_register[email]['last']:
                        if phone_b == back_register[email]['phone']:
                            print(f"{back_register[email]['password']:},")
                        else:
                            print("your data is incorrect \
please try again or create an account")
                    else:
                        print("your data is incorrect please \
try again or create an account")
                else:
                    print("your data is incorrect please try \
again or create an account")
            else:
                print("your data is incorrect please\
try again or create an account")


shop_list_you_choose = list()
shop_list_you_cost = list()



class Shop:
    """ """
    def __init__(self):
        self.item = None
        self.number = None
        self.shop_fruits: Dict = {"tomatoes": 2.4, "bananas": 3.1,
                                  "basil": 1.2, "coriander": 1.3,
                                  "radish": 1.1, "parsley": 0.8, "dill": 0.7,
                                  "mint": 1,
                                  "apple": 1.7, "orange": 2.4,
                                  "cucumber": 1.6, "kiwi": 1.55}
        self.shop_dairy_product: Dict = {"butter": 2.7, "cheese": 3.8,
                                         "milk": 1.5, "yoghurt": 2.3}

    def choose_item(self, item, number):
        """

        Parameters
        ----------
        item : item you want to chose  from our shop shop_fruits
            
        number : number that you you want you buy that item


        Returns a list of item and number
        -------

        """
        self.item = item
        self.number = number
        if self.item in self.shop_fruits:
            print("how much you want:")
            price_goods_one: float = self.shop_fruits.get(item)
            price_cost_one_item = self.number*price_goods_one
            print(f'{price_cost_one_item}you should cost for {self.item}')
            shop_list_you_choose.append(self.item)
            shop_list_you_cost.append(price_cost_one_item)
        else:
            print("you did not chose any item fruits")

    def price_cost_last(self):
        """ """
        last_price_you_cost = sum(shop_list_you_cost)
        print("last price :", last_price_you_cost)
        return last_price_you_cost

    def choose_item_diary(self, item, number):
        """

        Parameters
        ----------
        item : item you want from dairy_product

        number : number of that item


        Returns a list of item and  price
        -------

        """
        if item in self.shop_dairy_product:
            price_goods_one: float = self.shop_fruits.get(item)
            price_cost_one_item = number*price_goods_one
            print(f'{price_cost_one_item}you should cost for {item}')
            shop_list_you_choose.append(item)
            shop_list_you_cost.append(price_cost_one_item)
            price_goods_one_b: float = self.shop_fruits.get(item)
            print("price_goods_one_b", price_goods_one_b)
        else:
            print("you did not chose any item from fruits")

    def remove_shop(self, item, number):
        """

        Parameters
        ----------
        item : item you want to remove
            
        number : number item you want to remove
            

        Returns a price you should pay
        -------

        """
        dict_shop = dict(zip(shop_list_you_choose, price_goods_one_b))
        print("dict_shop", dict_shop)
        pay = self.price_cost_last()
        if item in dict_shop.keys():
            price_for_your_item = dict_shop.get(item)
            print("price_for_your_item", price_for_your_item)
            lost = number * price_for_your_item
            print("lost:", lost)
            x = pay - lost
            print("price you should cost :", x)


price_goods_one_b = {}
users_database = {}

while True:
    ask_user_login = input("please enter create/login :")
    if ask_user_login == "create":
        new_username = input("pleas enter your username:")
        last_name = input("please enter your last name :")
        new_email = input("please enter your email :")
        new_password = input("please enter your password:")
        phone = input("please enter your phone number :")
        person = User(new_username, last_name, new_email,
                      new_password, phone)
        break
    elif ask_user_login == "login":
        email = input("please enter your email :")
        password = input("please enter your password :")
        Create_account.check_logging(email, password)
        forgot = input("yse or no:")
        if forgot == "yes":
            print("you should enter your name,lastname,phone number\
to get your password and your email.")

            email = input("please enter your email :")
            name = input("please enter your name :")
            last_name = input("please enter your last name :")
            phone = input("please enter your phone number :")
            User.back_password(email, name, last_name, phone,
                               "login_users.json")
            break
        elif forgot == "no":
            break
    else:
        print("you should first login or create an account")
shop = Shop()
while True:
    print("if you want any help you should just write : help")
    buy_item: str = input("if you want to buy something please enter :\
yes if you dont want write no.?")
# you chose you item

    if buy_item == "yes":
        print("these are our shopping ")
        print("we have ,fruits,dairy products")
        goods: str = input("which kind of goods you want if you want fruits \
write 1  if you want dairy product write 2 : :")

        class Day(Enum):
            """ """
            fruits = "1"
            dairy_products = "2"
        list_fruits = Day.fruits.value
        list_dairy_products = Day.dairy_products.value
        # show the shopping
        if goods == list_fruits:
            print(shop.shop_fruits)
            item_shop = input("which kind of items you want :")
            if item_shop in shop.shop_fruits:
                number_shop = int(input("how much number is enough for you"))
                if number_shop != 100 or number_shop < 100:
                    print("ok")
                    shop.choose_item(item_shop, number_shop)
            print(shop_list_you_choose)
            print(shop_list_you_cost)
            shop.price_cost_last()
        elif goods == list_dairy_products:
            print(shop.shop_dairy_product)
            item_shop = input("which kind of items you want :")
            number_shop = int(input("how much number is enough for you :"))
            item_shop in shop.shop_dairy_product
            if (number_shop) <= 100:
                print("ok")
                shop.choose_item_diary(item_shop, number_shop)
            print(shop_list_you_choose)
            print(shop_list_you_cost)
        else:
            print("please enter correct word")
    if buy_item == "help":
        root = input("write each want you want ---->\
remove/done/i have some order :")
        if root == "remove":
            item_shop = input("which kind of items you want :")
            number_shop = int(input("how much number is enough for you :"))
            shop.remove_shop(item_shop, number_shop)
