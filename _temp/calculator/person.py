'''
 * @Process: complete
 * @Project_Name: module
 * @Package_Name: calculator
 * @Made_By: JS
 * @The_creation_time: --
 * @File_Name: person.py
 * @Version : Python 3.7.8
 * @contents: -
'''


class Person:    # 클래스
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('안녕하세요. 저는 {0}입니다.'.format(self.name))
