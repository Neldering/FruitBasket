Hello This is the fruitbasket application

it takes a csv file using the following headers (example of csv provided via fruitBasket.csv):

fruit-type,age-in-days,characteristic1,characteristic2

apple,1,red,sweet



Requires 
Python3
pip


TO RUN
using command line go to frutibasket folder
in fruitbasket folder you can run:
python -m fruitBasket process

it will prompt you for a csv file, provide the path to your csv file

it will give output to the console and make an output file as output.txt




ADDITIONAL COMMANDS
you can run the version and the help command via:

python -m fruitBasket -v

python -m fruitBasket --help

TESTING
you can run to run the tests under tests folder
python -m pytest tests/
