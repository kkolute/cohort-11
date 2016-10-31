class Car(object):


    def __init__(self,name='General', model='GM' ,type_of_car='saloon' ):
        self.type_of_car = type_of_car
        self.model = model
        self.name = name
        self.speed = 0

        if name== 'Porshe' or name== 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if type_of_car == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

    def drive(self, spd):
        if self.type_of_car == 'trailer':
            self.speed = spd * 11
        else:
            self.speed = 10 ** spd

        return self
        
    def is_saloon(self):
        if self.type_of_car =='saloon':
            return 'True'
        else:
            return 'False'