import os
import tempfile
class File:
    countfile = 0
    def __init__(self,path):
        self.path = self.retpathfile(path)
        self.__filestrm = None
    def retpathfile(self, path):
        if os.path.exists(path):
            return path
        else:
            f = open(path,"w")
            f.close()
            return path
    def read(self):
        f = open(self.path)
        out = f.read()
        f.close()
        return out
    def write(self, text):
        f = open(self.path,"w")
        count = f.write(text)
        f.close()
        return  count
    def __add__(self,other):
        f1 = open(self.path)
        f2 = open(other.path)
        text = f1.read()+f2.read()
        f1.close()
        f2.close()
        File.countfile += 1
        num = File.countfile
        new_path = os.path.join(tempfile.gettempdir(), f"newfile{num}.txt")
        new_file = File(new_path)
        new_file.write(text)
        return  new_file
    def __iter__(self):
        self.__filestrm = open(self.path)
        return self.__filestrm
    def __next__(self):
        out = self.__filestrm.readline()
        if out == "":
            self.__filestrm.close()
            self.__filestrm = None
            raise  StopIteration
        return out
    def __str__(self):
        return os.path.abspath(self.path)


if __name__ == '__main__':
    f1 = File("a.txt")
    f2 = File("b.txt")
    print(f1)
    f2.write("kekekek\n")
    f2.write("uuuuuuu")
    f3 = f1 + f2
    print(f3)
    for  i in f3:
        print(i)


