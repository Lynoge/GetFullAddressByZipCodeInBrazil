# GetFullAddressByZipCodeOnBrazil ![CI status](https://img.shields.io/badge/build-passing-brightgreen.svg)

GetFullAddressByZipCodeOnBrazil is a Python function that pass a input parameter (brazilian zip code) and get full address. The search is did on Correios official website.

## Motivation

I developed this function because I did need to get full address to cleaning/adjust the clients registers of database.

## Installation

### Requirements
* S.O.: Linux
* Python 3.3 and up

1 - Open Terminal

2 - Access your "home":
	cd /home/your_username/

3 - Clone the github repository:
	git clone https://github.com/daniellj/GetFullAddressByZipCodeOnBrazil

4 - Access the new folder created:
	cd GetFullAddressByZipCodeOnBrazil/

5 - Install the Dependencies: Python Libraries
	pip install -r requirements.txt

## Usage
1 - Call de function from the linux terminal command line:
	python -c 'import GetFullAddressByZipCodeOnBrazil as gt; print(gt.GetFullAddressByZipCodeOnBrazil("INPUT_ZIPCODE_TO_SEARCH"))'

The return is a python list, containing, in order, the following informations:

['Street/Avenue/Public Area', 'Neighborhood', 'City', 'State', 'ZipCode']

## Development
This function can be easily adapted for any system. Use it if necessary.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)