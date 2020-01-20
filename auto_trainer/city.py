
class City():

    def __init__(self, name, coords, img):
        self._name = name
        self._coords = coords
        self._img = img
    
    def get_name(self):
        return self._name
    
    def get_coords(self):
        return self._coords
    
    def get_img_name(self):
        return self._img
    
    def to_dictionary(self):
        return {
            "name": self._name,
            "coords": self._coords,
            "img": self._img
        }
    
    @staticmethod
    def from_dictionary(city_dict):
        name = city_dict["name"]
        coords = city_dict["coords"]
        img = city_dict["img"]
        return City(name, coords, img)