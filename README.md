# hacker_news_project

This Python script scrapes articles from the front page of Hacker News, a popular news aggregation website. It filters the articles based on their vote count, displaying only those with more than 99 votes. The script uses BeautifulSoup to parse the HTML content of the website and extracts relevant information such as article titles, links, and vote counts. It then sorts the articles by the number of votes in descending order and presents them to the user. Additionally, the script allows the user to fetch more news articles from subsequent pages of Hacker News if desired.
```
# Hacker News Scraper

This Python script allows you to scrape and view articles from Hacker News with a vote count greater than 99.

## Dependencies

- Python 3.x
- BeautifulSoup4
- requests

## Installation

1. Clone the repository:

```bash
git clone https://github.com/dracolich2000/hacker-news-scraper.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script `hacker_news_scraper.py`:

```bash
python hacker_news_scraper.py
```

The script will display articles from the front page of Hacker News with a vote count greater than 99. It will then prompt you if you want to read more news. Input 'y' to fetch more news or 'n' to quit.

## Customization

You can modify the vote count threshold by changing the value in the `create_custom_hn` function in the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Make sure to replace "your_username" in the GitHub repository link with your actual GitHub username, and adjust the content as needed. This README provides basic instructions on how to install and use the script, along with information about dependencies and customization options.
