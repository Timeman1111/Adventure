

class Shop:
    def __init__(self,shop_name,products = []):
        self.name = shop_name
        self.products = products

    def add_product(self,product):
        self.products.append(product)
        return True
    
    def remove_product(self,product_index):
        try:
            del self.products[product_index]
        except IndexError:
            return False
        else:
            return True


class Scene:
    def __init__(self,properties={},trace = None):
        # Initalize Scene and set class variables
        
        self.trace = trace
        self.properties = properties

    def set_location_text(self,text):
        #Set scene location text

        self.properties["location_setting_text"] = text

        
        return True


    def get_scene(self):

        # Get location setting from class property variable
        location_setting = self.properties["location_setting_text"]

        #Get shop data from class property variable and then get the names
        shops = self.properties["shops"]

        shops_names = [x["name"] for x in shops]

Library = Scene()
