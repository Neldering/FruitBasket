Hello This is the fruitbasket application

it takes a csv file using the following format (example of csv provided below):

fruit-type,age-in-days,characteristic1,characteristic2
apple,1,red,sweet
orange,2,round,sweet
pineapple,5,prickly,sweet
apple,4,yellow,sweet
grapefruit,2,yellow,bitter
watermelon,4,green,heavy
orange,2,round,sweet
orange,1,round,sweet
pineapple,6,prickly,sweet
apple,1,green,tart
grapefruit,1,bitter,yellow
watermelon,2,heavy,green
grapefruit,2,bitter,yellow
watermelon,3,heavy,green
orange,1,round,sweet
orange,5,sweet,round
pineapple,2,sweet,prickly
apple,2,red,sweet
orange,6,round,sweet
pineapple,2,sweet,prickly
apple,1,red,sweet
grapefruit,3,yellow,bitter


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
