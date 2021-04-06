# Scrap_Book_Data
Scraps the information about the books and stores it in a formatted CSV file.

Base URL from which data is scraped: https://www.goodbooks.io/books
<br>

## Installing requirements
```
pip install -r requirements.txt
```
## Running Python Script
```
python scraping.py
```
### Output of above command
```
[POST] Fetching Info...
[POST] Total Pages:  229
[POST] Books in each page:  24
[GET] Enter Start Page:
```
> Enter the start page range and end page range.

```
[POST] Fetching Info...
[POST] Total Pages:  229
[POST] Books in each page:  24
[GET] Enter Start Page: 1
[GET] Enter End Page: 10
```

> After entering valid page range, you will get following messages which confirms that your data is scraped and stored in corresponding csv file in ```Scrapped-data``` folder.

```
[POST] Fetching Info...
[POST] Total Pages:  229
[POST] Books in each page:  24
[GET] Enter Start Page: 1
[GET] Enter End Page: 10
[POST] Scraping Page - 1 data in file named 1.csv.
[POST] Data for page-1 stored in ./Scraped-data/1.csv.
[POST] Scraping Page - 2 data in file named 2.csv.
[POST] Data for page-2 stored in ./Scraped-data/2.csv.
[POST] Scraping Page - 3 data in file named 3.csv.
[POST] Data for page-3 stored in ./Scraped-data/3.csv.
[POST] Scraping Page - 4 data in file named 4.csv.
[POST] Data for page-4 stored in ./Scraped-data/4.csv.
[POST] Scraping Page - 5 data in file named 5.csv.
[POST] Data for page-5 stored in ./Scraped-data/5.csv.
[POST] Scraping Page - 6 data in file named 6.csv.
[POST] Data for page-6 stored in ./Scraped-data/6.csv.
[POST] Scraping Page - 7 data in file named 7.csv.
[POST] Data for page-7 stored in ./Scraped-data/7.csv.
[POST] Scraping Page - 8 data in file named 8.csv.
[POST] Data for page-8 stored in ./Scraped-data/8.csv.
[POST] Scraping Page - 9 data in file named 9.csv.
[POST] Data for page-9 stored in ./Scraped-data/9.csv.
[POST] Scraping Page - 10 data in file named 10.csv.
[POST] Data for page-10 stored in ./Scraped-data/10.csv.
```
## Technology Used
* [Python with BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Conclusion
Data like book title, book author, book cover url, Amazon url and apple books url is scraped ```page by page``` from the ```base_url``` as per user's choice and stored in well-formatted manner in CSV files with appropriate file names. 
