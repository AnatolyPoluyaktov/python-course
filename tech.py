import os
import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
    def get_photo_file_ext(self):
        root, ext = os.path.splitext(self.photo_file_name)
        return ext


class Car(CarBase):
    car_type ="car"
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    car_type = "truck"
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)

        try:

            self.body_length, self.body_width, self.body_height = map(lambda x: float(x), body_whl.split("x"))
        except:
            self.body_length, self.body_width, self.body_height =map(lambda x: float(x),[0,0,0] )


    def get_body_volume(self):
        v = self.body_height * self.body_length * self.body_width
        return v



class SpecMachine(CarBase):
    car_type="spec_machine"

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra



def get_car_list(csv_filename):
    if os.stat(csv_filename).st_size == 0:
        return []
    car_list = []
    e =[".jpeg",".jpg",".png",".gif"]
    type_car = ["car","truck","spec_machine"]
    with open(csv_filename) as csv_df:
        reader = csv.reader(csv_df, delimiter=';')
        next(reader)
        for row in reader:
            if len(row) == 7:

                car_type , brand, passenger_seats_count,\
                photo_file_name,body_whl,carrying, extra = row
                if car_type and photo_file_name and brand and carrying:
                    try:
                        root, ext = os.path.splitext(photo_file_name)
                        if ext not in e:
                            raise ValueError

                        carrying = float(carrying)
                        if carrying <=0:
                            raise ValueError
                    except ValueError:
                        continue
                    if  car_type =="car":
                        if not body_whl and not extra:
                            try:
                                car_list.append(Car(brand,photo_file_name,carrying, int(passenger_seats_count)))
                            except ValueError:
                                continue


                    elif car_type == "truck":
                        if not passenger_seats_count and not extra:
                            car_list.append(Truck(brand, photo_file_name, carrying, body_whl))

                    elif car_type == "spec_machine":
                        if not passenger_seats_count and not body_whl and extra:
                            car_list.append(SpecMachine(brand,photo_file_name,carrying,extra))

                else:
                    pass


    return car_list

if __name__ == "__main__":
    l = get_car_list("a.csv")

    print(type(l[0]))
    c= Truck('Toyota', 't2.jpeg', '3.0', '3.7x2x2.6x')
    print(type(c.body_height))