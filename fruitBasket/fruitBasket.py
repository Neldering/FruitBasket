
from pathlib import Path
import csv
import pandas as pd



validHeaders = ['fruit-type', 'age-in-days', 'characteristic1', 'characteristic2']
outputReport = 'output.txt'

class ActiveBasket:
    def process() -> None:
        prompt = input("\nHello welcome to Fruit basket,"
        "\n \nPlease type in the path to your file and press 'Enter': ")
        try:
            with open(outputReport, 'w') as filetowrite:
                with open(prompt, 'r') as file:
                    #reader = csv.reader(file)
                    data = pd.read_csv(file)
                    #print(data)
					
					#validate headers
                    if((data.columns.values.tolist() != validHeaders)):
                        print("invalid headers ")
                        print("headers must be in following format: " )
                        print(validHeaders)
                        raise ValueError("invalid headers")
                    #raise ValueError("custom")
					
					#count of fruit
                    print('\nTotal number of fruit:')
                    print(str(len(data)) +'\n \n')
                    #filetowrite.write(data.to_string() +'\n')
                    filetowrite.write('Total number of fruit:' + '\n')
                    filetowrite.write(str(len(data)) + '\n \n')
					
					
					#count of fruit types
                    print('Total types of fruit:')
                    byType = data.groupby('fruit-type')
                    print(str(len(byType)) +'\n \n')
                    filetowrite.write('Total types of fruit:' + '\n')
                    filetowrite.write(str(len(byType)) + '\n \n')


					#oldest fruit and age
                    print('Oldest fruit & age:')
                    oldestNum = data[['age-in-days']].max(numeric_only=True)
                    oldest = data.loc[data['age-in-days'] == int(oldestNum)]
                    oldest = oldest.drop('characteristic1', axis=1).drop('characteristic2', axis=1)
                    print(oldest.to_string(index=False) +'\n \n')
                    filetowrite.write('Oldest fruit & age:' + '\n')
                    filetowrite.write(oldest.to_string(index=False) + '\n \n')
					
					
                    #the number of each type of fruit in decending order (fruit then count)
					
                    print('The number of each type of fruit in descending order:')
                    byTypeCount = data.groupby(['fruit-type'])['fruit-type'].count().reset_index(name='count').sort_values(['count'], ascending=False)
                    print(byTypeCount.to_string(index=False) +'\n \n')
                    filetowrite.write('The number of each type of fruit in descending order:' + '\n')
                    filetowrite.write(byTypeCount.to_string(index=False) +'\n \n')

					#the various charactersticts of each fruit by type 
                    print('The various characteristics (count, color, shape, etc.) of each fruit by type:')
                    byTypeAndChar = data.groupby(['fruit-type', 'characteristic1', 'characteristic2'])['fruit-type'].count().reset_index(name='count').sort_values(['count'], ascending=False)
                    print(byTypeAndChar.to_string(index=False) + '\n \n')
                    filetowrite.write('The various characteristics (count, color, shape, etc.) of each fruit by type:' + '\n')
                    filetowrite.write(byTypeAndChar.to_string(index=False) + '\n \n')
					
					
                    filetowrite.close()					

                
        except Exception as ex:
            print(ex)
            raise ex