
class FileReader:
    def __init__(self, filename):
        self.filename = filename
    def read(self):
        try:
            fd = open(self.filename, 'r')

        except FileNotFoundError:
            return ''
        else:
            ans =fd.read()
            fd.close()
            return ans


if __name__ == "__main__":
    file = open("a.txt","w")
    file.write("privet")
    file.close()
    file = FileReader("b.txt")
    a=file.read()
    print("k"+a*10+"K")