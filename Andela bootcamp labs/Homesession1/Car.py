'''
author : Kennedy kolute
class  : Andela bootcamp 11
'''
class Car(object):
# car constructor initializes the object variables
    def __init__(self, name='General', model='GM', type='saloon'):
        self.type = type
        self.model = model
        self.name = name
        self.speed = 0
		
        # set object variables depending on the name and type of the car object

        if name == 'Porshe' or name == 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4
	

    def drive(self, spd):
	# set speed of car by type
        if self.type == 'trailer':
            self.speed = spd * 11
        else:
            self.speed = 10 ** spd

        return self

    def is_saloon(self):
        if self.type == 'saloon':
            return 'True'
        else:
            return 'False'