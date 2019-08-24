# REST_PyNav
A Python GUI Application using REST/JSON/PyQT5.

## What this Application does

This Application is basically a simplified Google Maps written in Python using the MVC Design Pattern. 
The Controller Class combines the Model Class in this project since the model is so slim anyways. 
This App makes a REST GET request to the Google Directions API which fetches the data of directions between two locations. 
The JSON data is then parsed into a humanly readable form (which is the actual hard part) and displayed on the UI.

### Prerequisites

This Application is using PyQT5 so you need need to install it using pip since its not included in the standard Python libraries. 
Other than that its pure Python code with some included standard libraries like requests and json.

```
pip install PyQT5
```
