import json



class NPC:

  def __init__(self,name):


    self.name = name

    self.dialog = {}


  def request_line(self,line_num):
    #Request line and serve it and the responses to the player

    line_data = {}


    #Get dialog info from loaded json
    dialogInfo = self.dialog[str(line_num)]


    #Get responses and import them into line_data for game
    responses = dialogInfo["options"]

    line_data['responses'] = responses

    #Get text line for the game
    line = dialogInfo['line']

    line_data['text'] = line

    return line_data

    

  def import_dialog(self,json_file):

    f = open(json_file,'r')


    data = json.load(f)
    self.dialog = data

    return True