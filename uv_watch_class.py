import turtle as t

class UVWatch():

    def __init__(self, temperature, heart_rate_bpm, absorbtion_wavelength_levels, wavelength):
        self.temperature = str(temperature)
        self.absorbtion_wavelength_levels = str(absorbtion_wavelength_levels)
        self.heart_rate_bpm = str(heart_rate_bpm)
        self.uv_wavelength = int(wavelength)
        self.records = [self.temperature, self.absorbtion_wavelength_levels, self.heart_rate_bpm]
        self.input_list = ['temp', 'heart_rate_bpm', 'absorbtion_wavelength_levels']
        

    def get_temperature(self):
        #placeholder
        return self.temperature
        pass

    def get_wavelength(self):
                #placeholder
        return self.absorbtion_wavelength_levels
        pass

    def get_bpm(self):
                #placeholder
        return self.heart_rate_bpm
        pass

    def change_wavelength(self):
        loop_var = True
        while loop_var == True:
            user_input = input('Type a number for the wavelength:')
            try:
                self.uv_wavelength = int(user_input)
                loop_var = False
            except ValueError:
                print('oops, thats not a number, try again!')
            

    def print_inputs(self):
        for i in range(0, len(self.input_list)):
            print('Your ' + self.input_list[i] + ' levels are ' + str(self.records[i]))

    def display_results(self):
            screen = t.Screen()
            if self.uv_wavelength >= 300 and self.uv_wavelength <=320:
                screen.bgcolor('blue')
            elif self.uv_wavelength >= 321 and self.uv_wavelength <=340:
                screen.bgcolor('green')
            elif self.uv_wavelength >= 341 and self.uv_wavelength <= 360:
                screen.bgcolor('yellow')
            elif self.uv_wavelength >= 361 and self.uv_wavelength <= 380:
                screen.bgcolor('orange')
            elif self.uvwavelength >= 381 and self.uv_wavelength <= 400:
                self.bgcolor('red')
	    else:
		#placeholder, should pop up with a screen saying the number is out of range
		pass

my_watch = UVWatch('98', '100', '32', 390)
my_watch.change_wavelength()
my_watch.display_results()
            

