class Person:
    def __init__(self, fname=None, lname=None, email=None, phone=None):
        self.__fname = fname
        self.__lname = lname 
        self.__email = email
        self.__phone = phone
 

    def set_fname(self, fname):
        self.__fname = fname
    def get_fname(self):
        return self.__fname
    def set_lname(self, lname):
        self.__lname = lname
    def get_lname(self):
        return self.__lname
    def set_email(self, email):
        self.__email = email
    def get_email(self):
        return self.__email
    def set_phone(self, phone):
        self.__phone = phone
    def get_phone(self):
        return self.__phone
  



