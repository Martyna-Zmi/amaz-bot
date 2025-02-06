# Amaz-bot
A Python + Selenium web bot designed to quickly input form data from a csv file. It can be used for testing web applications or automatization of providing product descriptions for online sellers

*Disclaimer: this project is made for educational purposes only*

## How it works:
Each line in data.csv contains three parameters - attribute type, attribute name and input value
For example a line like: id;surname;Smith - searches for an HTML input tag with id equal to surname and fills it with value "Smith"
One data file can contain multiple values
