class Coffee():

    def __int__(self, id, name, address, city, state, zip, lat, lon):
        self.id = id
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return "id: {} name: {} address: {} city: {} state: {} zip: {} lat: {} lon: {}".format(self.id, self.name,
                                                                                               self.address, self.city,
                                                                                               self.state, self.city,
                                                                                               self.zip, self.lat,
                                                                                               self.lon)
