class UVWatch():

	def __init__(self, temperature, heart_rate_bpm, absorbtion_wavelength_levels):
		self.temperature = str(temperature)
		self.absorbtion_wavelength_levels = str(absorbtion_wavelength_levels)
		self.heart_rate_bpm = str(heart_rate_bpm)
		self.records = [self.temperature, self.absorbtion_wavelength_levels, self.heart_rate_bpm]
		self.input_list = ['temp', 'heart_rate_bpm', 'absorbtion_wavelength_levels']

	def get_temperature(self):
		#placeholder
		return self.temperature
		pass

	def get_wavelength(self):
		return self.absorbtion_wavelength_levels
		pass

	def get_bpm(self):
		return self.heart_rate_bpm
		pass

	def print_inputs(self):
		for i in range(0, len(self.input_list)):
			print('Your ' + self.input_list[i] + ' levels are ' + str(self.records[i]))


my_uv_watch = UVWatch('18','20','14')
my_uv_watch.print_inputs()