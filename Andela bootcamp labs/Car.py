class Car(object):


    def __init__(self,name='General', model='GM' ,type='honda' ):
        self.type = type
        self.model = model
        self.name = name
        self.speed = 0

        if name== 'Porshe' or name== 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

    def doors(self, num_of_doors):
        pass

    def drive(self, moving_man):
        return moving_man

    def drive(self, spd):
        if self.type == 'trailer':
            self.speed = spd * 11
        else:
            self.speed = 10 ** spd

        return self

    def wheels(self, num_of_wheels):
        return num_of_wheels


    def is_saloon(self):
        if self.type ==  'trailer':
            return False
        else:
            return True