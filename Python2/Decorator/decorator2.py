class Greet(object):
    current_user = None
    def set_name(self, name):
        if name == "admin":
            self.current_user = name
        else:
            raise Exception("There is no access authtorization")

    def get_greeting(self, name):
        if name == "admin":
            return "Hello {}".format(self.current_user)

greet = Greet()
greet.set_name("admin")
greet.get_greeting("yeongseon")
        