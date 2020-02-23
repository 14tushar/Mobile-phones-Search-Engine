# Mobile phones Search Engine
Search mobile phones by applying filters on various specifications like Camera, RAM, Company. It searches through a database which is generated using a web-scraper. It retrieves the data of all the mobile phones and their specifications from the flipkart.com website and store the relevant information in the respective column in the database.
<br>

#### Running the script
The code is in python3. Thus, python3 must be installed in the system to run the script.
* Install urllib Library (if not installed)
* Install BeautifulSoup Library using [pip install beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
<br>

#### Technology Used
| Description | Technology |
|---|----|
| Scripting Language | Python |
| Database | SQLite |
| Library for webscraping | BeautifulSoup |
| Library for webcrawling | URLLib |
|---|---|
<br>

#### Screenshots:
The FLIPKART_DATA.py script scrapes the data from flipkart.com Mobile Phone section and displays the total number of rows added to the database uptil now.
![Execution of FLIPKART_DATA.py](/assets/FLIPKART_DATA_EXECUTION.png | width=200)<br /><br /><br />

The database updated by the above script has 2 tables:
1) Mobile: Contains the Name, Price, and Rating of the mobile.
![Mobiles Table in database](/assets/Mobile_Table.png "Mobiles Table")

2) Specs: Contains around 140 specifications of the mobile phone.
![Specifications Table in database](/assets/SPECIFICATIONS_TABLE.png "Specs Table")<br /><br /><br />

The flipkart_search.py allows to enter the name of the mobile phone and returns the relevant results from flipkart.
![Execution of flipkart_search.py](/assets/Flipkart_search_execution.png "flipkart_search.py Execution")

#### To be included...
* The prices of the mobile phones will be scraped from various online markets and the search engine will allow to compare the prices of a product on different markets.
* Machine Learning will be applied to the dataset to predict the price for the new mobile phones to be launched by a company. And thereafter, giving recommendations of the phones with best specifications at lower price.

