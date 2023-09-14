class Shop:

  def __init__(self, shop_name, products=[]):
    #Initalize shop class

    self.name = shop_name

    #Check and fix products incase only one object is used.
    if type(products) != list:

      self.products = []
      
      self.products.append(products)
    

  def add_product(self, product):
    #Add single product item to shop category if item is a dictonary
    if type(product) == dict:

      self.products.append(product)

      #Else return negative status
    else:
      return False

    #Return true
    return True
  
  def add_products(self,products):
    #Add multiple products to shop using list or otherwise.
    if type(products) == list:

      self.products.extend(products)

    else:
      return False
    
  def remove_product(self, product_index):

    #Remove item from the product list
    try:

      del self.products[product_index]

      #If item is not in list raise error and return false
    except IndexError:
      return False
    else:

      #Return True otherwise
      return True


#Main Scene Class variable
class Scene:

  def __init__(self, properties={}, trace=None):
    # Initalize Scene and set class variables

    self.trace = trace
    self.properties = properties
    try:
      self.properties['shops']
    except:
      self.properties['shops'] = []

  def set_location_text(self, text):
    #Set scene location text

    self.properties["location_setting_text"] = text

    return True

  def get_scene(self):

    # Get location setting from class property variable
    location_setting = self.properties["location_setting_text"]

    #Get shop data from class property variable and then get the names
    shops = self.properties["shops"]

    #Get shop names
    shops_names = [x["name"] for x in shops]

  def add_shop(self, shop):

    #Add shop to scene
    self.properties["shops"].append(shop)

    return True
