from bs4 import BeautifulSoup
import requests
import os

def main(URL, output_file):
    # specifying user agent
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    }

    try:
        # Making the HTTP Request
        webpage = requests.get(URL, headers=HEADERS)
        webpage.raise_for_status()  # Raise HTTPError for bad responses
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return

    # Creating the Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "lxml")

    # opening our output file in append mode
    with open(output_file, "a") as file:
        # retrieving product title
        try:
            title = soup.find("span", attrs={"id": 'productTitle'}).get_text(strip=True).replace(',', '')
        except AttributeError:
            title = "NA"
        print("Product Title =", title)
        file.write(f"{title},")

        # retrieving price
        try:
            price = soup.find("span", attrs={'id': 'priceblock_ourprice'}).get_text(strip=True).replace(',', '')
        except AttributeError:
            price = "NA"
        print("Product Price =", price)
        file.write(f"{price},")

        # retrieving product rating
        try:
            rating = soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).get_text(strip=True).replace(',', '')
        except AttributeError:
            try:
                rating = soup.find("span", attrs={'class': 'a-icon-alt'}).get_text(strip=True).replace(',', '')
            except AttributeError:
                rating = "NA"
        print("Overall Rating =", rating)
        file.write(f"{rating},")

        # retrieving review count
        try:
            review_count = soup.find("span", attrs={'id': 'acrCustomerReviewText'}).get_text(strip=True).replace(',', '')
        except AttributeError:
            review_count = "NA"
        print("Total Reviews =", review_count)
        file.write(f"{review_count},")

        # retrieving availability status
        try:
            available = soup.find("div", attrs={'id': 'availability'}).find("span").get_text(strip=True).replace(',', '')
        except AttributeError:
            available = "NA"
        print("Availability =", available)
        file.write(f"{available},\n")

if __name__ == '__main__':
    # Define paths
    base_dir = r"C:\Users\Victus\OneDrive\Desktop\PRODIGY internship"
    url_file_path = os.path.join(base_dir, "url.txt")
    output_file_path = os.path.join(base_dir, "out.csv")

    # Check if `url.txt` exists
    if not os.path.exists(url_file_path):
        print(f"{url_file_path} not found. Please ensure the file is in the correct directory.")
    else:
        # opening our url file to access URLs
        with open(url_file_path, "r") as file:
            # iterating over the urls
            for links in file.readlines():
                main(links.strip(), output_file_path)
