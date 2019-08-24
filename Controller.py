import sys, requests, json
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import *
from View import View


class Controller(QWidget):
    """
    Controller Class of the MVC Pattern. Merged with Model since its just a few methods.
    Initializes the GUI and makes a REST GET Request to the Google Directions API for some instructions like in Google Maps
    """

    def __init__(self, parent=None):
        #setup UI
        super().__init__(parent)
        self.view = View()
        self.view.setupUi(self)

        # connect buttons
        self.view.resetButton.clicked.connect(lambda: self.reset())
        self.view.submitButton.clicked.connect(lambda: self.submit())


    def submit(self):
        # set params, make request
        url = "https://maps.googleapis.com/maps/api/directions/json"
        parameter = {"origin": self.view.fromText.text(),
                     "destination": self.view.toText.text(),
                     "sensor": "false",
                     "language": "EN",
                     "key": "AIzaSyBx534-Og1664FDBkr9AtLJvWjWLsJKaOM"  # has most likely expired at this point, you have to provide your own API KEY (its free)
                     }
        route = requests.get(url, params=parameter)
        print(route)  # if code 200 == Request OK, if code == 400 -> Request Error

        # convert/parse the json response to a string output
        response = route.json()
        output = ""
        output += "The total est. time is: <b>" + response['routes'][0]['legs'][0]['duration'][
            'text'] + "</b>, the total Distance is: <b>" + response['routes'][0]['legs'][0]['distance'][
                   'text'] + "</b><br><br>"
        for i in response['routes'][0]['legs'][0]['steps']:
            output += i['html_instructions']
            output += ", Distance: " + i['distance']['text']
            output += ", Est. Time: " + i['duration']['text']
            output += "<br>"

        self.view.routeText.appendHtml(output)

    def reset(self):
        self.view.fromText.setText("")
        self.view.toText.setText("")
        self.view.routeText.setPlainText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    c = Controller()
    c.show()
    sys.exit(app.exec_())