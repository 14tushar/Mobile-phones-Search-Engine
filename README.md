# Mobile phones Search Engine
A database of all the mobile phones and their specifications is created using a web-scrapping script which retrieve the data from the flipkart.com website. This database is used for searching a phone by applying filters on different specifications.

#### Initialization

The code is in python3. Thus, python3 must be installed in the system to run the script.
* Install urllib Library (if not installed)
* Install BeautifulSoup Library using [pip install beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

#### Technology Used

The database is created using sqlite and the data is scrapped from the flipkart.com website using BeautifulSoup library. The specifications of each mobile is extracted from its page and updated to the database. The FLIPKART_DATA.py script creates the tables if it doesn't exist already and extracts the data of the mobile phones that isn't in the table yet. Whenever new mobile phones are updated to the website, the database can be updated by executing that script. The script will first check the database, if the same model of the mobile exists or not and will insert the model that doesn't exist.

#### To be included...

* The prices of the mobile phones will be scraped from various online markets and the search engine will allow to compare the prices of a product on different markets.
* Machine Learning will be applied to the dataset to predict the price for the new mobile phones to be launched by a company. And thereafter, giving recommendations of the phones with best specifications at lower price.

#### Screenshots:
The FLIPKART_DATA.py script scrapes the data from flipkart.com Mobile Phone section and displays the total number of rows added to the database uptil now.
![Execution of FLIPKART_DATA.py](/assets/FLIPKART_DATA_EXECUTION.png "FLIPKART_DATA.py Execution")<br /><br /><br />

The database updated by the above script has 2 tables:
1) Mobile: Contains the Name, Price, and Rating of the mobile.
![Mobiles Table in database](/assets/Mobile_Table.png "Mobiles Table")

2) Specs: Contains around 140 specifications of the mobile phone.
![Specifications Table in database](/assets/SPECIFICATIONS_TABLE.png "Specs Table")<br /><br /><br />

The flipkart_search.py allows to enter the name of the mobile phone and returns the relevant results from flipkart.
![Execution of flipkart_search.py](/assets/Flipkart_search_execution.png "flipkart_search.py Execution")

