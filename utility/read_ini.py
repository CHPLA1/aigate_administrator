import configparser


class ReadIni(object):
    def __init__(self, file_name=None, node=None):
        if file_name == None:
            file_name = 'E:/code/PyChram_python/aigate_login/config/LocalElement.ini'
        if node == None:
            self.node = 'LoginElement'
        else:
            self.node = node
        self.cf = self.load_ini(file_name)

    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return  cf

    def get_value(self, key):
        data = self.cf.get(self.node, key)
        return data


if __name__ == '__main__':
    read_ini = ReadIni()
    print(read_ini.get_value('username_error'))
