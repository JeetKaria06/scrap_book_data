from bs4 import BeautifulSoup
import requests
import csv

base_url = "https://www.goodbooks.io/books"

print("[POST] Fetching Info...")
response = requests.get(base_url)

soup = BeautifulSoup(response.text, 'html.parser')

soup = soup.find('div', {'class':'sidebar-main'}).find('div', {'class':'collection w-dyn-list'})

books = soup.find_all('div', {'class':'children-perspective w-dyn-item'})
pages = soup.find('div', {'class':'w-page-count page-count'})
link_id = soup.find('a', {'class':'w-pagination-next pagination-btn'})

total_pages = int(pages.text.split('/')[1].strip())

print("[POST] Total Pages: ", total_pages)
print("[POST] Books in each page: ", len(books))

start_page = int(input("[GET] Enter Start Page: "))
end_page = int(input("[GET] Enter End Page: "))

# Validating page range
if(start_page>end_page or start_page<0 or end_page>total_pages):
    print("[POST] Enter Valid Parameters!")
    exit(0)

for page in range(start_page-1, end_page):
    print('[POST] Scraping Page -', page+1,'data in file named '+str(page+1)+'.csv.')
    
    with open('Scraped-data/'+str(page+1)+'.csv', 'w', encoding='utf-8') as csvfile:
        
        # QUOTE_MINIMAL quotes only those field which contains quotechar in it.
        Writer = csv.writer(csvfile, quotechar=',', quoting=csv.QUOTE_MINIMAL)
        Writer.writerow(['Title', 'Author', 'Book_info_url', 'Book_cover_url', 'Amazon_url', 'Apple_book_url'])

        url = base_url+link_id['href'][:-1]+str(page+1)

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        soup = soup.find('div', {'class':'sidebar-main'}).find('div', {'class':'collection w-dyn-list'})

        books = soup.find_all('div', {'class':'children-perspective w-dyn-item'})

        for book in books:
            book_title = book.find('h5', {'class':'grid-item-title'}).text.strip().strip(',').replace(',', ';')
            book_author = book.find('h6', {'class':'grid-item-subtitle'}).text.strip().strip(',').replace(',', ';')
            
            url = base_url+book.find('a', {'class':'book w-inline-block'})['href'][6:]

            amazon_url = ''
            apple_books_url = ''
            book_cover_url = ''
            if book.find('a', {'class':'btn-affiliate btn-affiliate-book btn-affiliate-book-sidebar w-inline-block'}):
                amazon_url = book.find('a', {'class':'btn-affiliate btn-affiliate-book btn-affiliate-book-sidebar w-inline-block'})['href']
            if book.find('a', {'class':'btn-affiliate btn-affiliate-book w-inline-block'}):
                apple_books_url = book.find('a', {'class':'btn-affiliate btn-affiliate-book w-inline-block'})['href']
            
            if book.find('img', {'class':'book-cover'}):
                book_cover_url = book.find('img', {'class':'book-cover'})['src']
            
            Writer.writerow([book_title, book_author, url, book_cover_url, amazon_url, apple_books_url])
        
        print('[POST] Data for page-'+str(page+1)+' stored in ./Scraped-data/'+str(page+1)+'.csv.')