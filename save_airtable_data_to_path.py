#import modules
import pandas as pd
import airtable as at
import os
from datetime import date
from dotenv import load_dotenv

#dotenv is a package that is going to look for .env file in my default enviornment and it's going to load the variables in the file
load_dotenv() 
DATA_REPO = os.getenv('DATA_REPO') #write what exactly is in the .env file in the (' ') or it won't load and store the variables
TOKEN = os.getenv('AIRTABLE_TOKEN')
BASE_ID = os.getenv('AIRTABLE_TEST_BASE_ID')

#connect to airtable using the airtable table name (Table) and table token number (TOKEN)
test_table = at.Airtable(BASE_ID, 'Table', TOKEN)
test1 = pd.DataFrame(test_table.get_all())
test1 = test1.merge(pd.json_normalize(test1['fields']), left_index=True, right_index=True)

#create a new folder on my desktop that is labeled as today's date
today = date.today(
new_dir = '/Users/kai/Desktop/' + str(today)
os.mkdir(new_dir)

#save the airtable data to the newly created folder
test1.to_csv(new_dir + '/test_table1.csv')
