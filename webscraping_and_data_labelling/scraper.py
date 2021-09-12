import argparse
import csv
import itertools
import logging
import time

import requests
import yaml
from bs4 import BeautifulSoup

logging.root.setLevel(logging.INFO)


ENV = # TODO: Load `env.yml` using yaml into an `ENV` variable
ALL_CATEGORIES = ENV["CATEGORY_URLS"] 
# TODO: In `env.yml`, add the other categories and their URLS


def get_parser() -> argparse.ArgumentParser:
    """
    parse command line arguments

    returns:
        parser - ArgumentParser object
    """
    parser = argparse.ArgumentParser(description="BBC Pidgin Scraper")
    parser.add_argument(
        "--output_file_name",
        type=str,
        default="bbc_pidgin_corpus.csv",
        help="Name of output file",
    )
    # TODO: Add your other command line arguments!
    #   Be sure to include their types & any default values.
    return parser


def get_page_soup(url: str):
    """
    Makes a request to a url and creates a beautiful soup object from the response html

    input:
        :param url: input page url
    returns:
        - page_soup: beautiful soup object from the response html
    """

    response = requests.get(url)
    # TODO: Complete the function to parse and return the page
    return None


def get_valid_urls(category_page: BeautifulSoup):
    """
    Gets all valid urls from a category page

    input:
        :param: url: category_page
    returns:
        - valid_urls: list of all valid article urls on a given category page
    """
    all_urls = category_page.findAll("a")
    valid_article_urls = []
    for url in all_urls:
        href = url.get("href")
        # from a look at BBC pidgin's urls, they always begin with the following strings.
        # so we obtain valid article urls using these strings
    return list(set(valid_article_urls))


def get_urls(category_url: str, category: str, time_delay: bool) -> list:
    """
    # TODO: Complete the docstring for this function
    """
    page_soup = get_page_soup(category_url)
    category_urls = get_valid_urls(page_soup)

    # get total number of pages for given category
    article_count_span = page_soup.find_all(
        "span", attrs={"class": "lx-pagination__page-number qa-pagination-total-page-number"}
    )
    # if there are multiple pages, get valid urls from each page
    # else just get the articles on the first page
    if article_count_span:
        total_article_count = int(article_count_span[0].text)
        logging.info(f"{total_article_count} pages found for {category}")
        logging.info(f"{len(category_urls)} urls in page 1 gotten for {category}")

        for count in range(1, total_article_count):
            # TODO: Use your `get_page_soup` and `get_valid_urls` functions
            #   to obtain valid urls from all pages
            logging.info(f"{len(page_urls)} urls in page {count + 1} gotten for {category}")
            category_urls += page_urls
            if time_delay:
                time.sleep(10)
    else:
        logging.info(f"Only one page found for {category}. {len(category_urls)} urls gotten")

    return category_urls


def get_article_data(article_url: str) -> tuple:
    """
    Obtains paragraphs texts and headlines input url article

    input:
        :param article_url: category_page
    returns:
        - headline: headline of url article
        - story_text: text of url article
        - article_url: input article url
    """
    page_soup = get_page_soup(article_url)
    # TODO: Locate the headline element
    headline = page_soup.find(
        "h1", attrs={"class": "<insert_class_name>"}
    )
    
    if headline:
        # TODO: Get the headline text from the element

    story_text = " "
    story_div = None    # TODO: Locate all story divs
    if story_div:
        all_paragraphs = [div.findAll("p", recursive=False) for div in story_div]
        all_paragraphs = list(itertools.chain(*all_paragraphs))
        story_text = story_text.join(str(paragraph) for paragraph in all_paragraphs)
        story_text = BeautifulSoup(story_text, "html.parser").get_text()
    story_text = story_text if not story_text == " " else None

    return headline, story_text, article_url


def scrape(output_file_name: str, no_of_articles: int, category_urls: dict, time_delay: bool) -> None:
    """
    Main function for scraping and writing articles to file

    input:
        :param output_file_name: file name where output is saved
        :param no_of_articles: number of user specified articles to scrape
        :param category_urls: all articles in a category
    """
    logging.info("Writing articles to file...")

    with open(output_file_name, "w") as csv_file:
        # TODO: Initialize a csv.DictWriter object
        #   Write the headers your CSV file will take
        story_num = 0

        for category, urls in category_urls.items():
            logging.info(f"Writing articles for {category} category...")
            for url in urls:
                # TODO: Get the headline, paragraphs and url using your `get_article_data` func
                headline, paragraphs, url = None, None, None
                if paragraphs:
                    # TODO: Write all the data to CSV
                    story_num += 1
                    logging.info(f"Successfully wrote story number {story_num}")

                if story_num == no_of_articles:
                    logging.info(
                        f"Requested total number of articles {no_of_articles} reached"
                    )
                    logging.info(
                        f"Scraping done. A total of {no_of_articles} articles were scraped!"
                    )
                    return
                if time_delay:
                    time.sleep(10)
    logging.info(
        f"Scraping done. A total of {story_num} articles were scraped!"
    )


# TODO: Based on this block, complete `get_parser`
if __name__ == "__main__":

    logging.info("--------------------------------------")
    logging.info("Starting scraping...")
    logging.info("--------------------------------------")

    # initialize parser
    parser = get_parser()
    params, unknown = parser.parse_known_args()

    # specify categories to scrape
    if params.categories != "all":
        categories = params.categories.upper().split(",")
        categories = {category: ALL_CATEGORIES[category] for category in categories}
    else:
        categories = ALL_CATEGORIES

    # get urls
    category_urls = {}
    for category, url in categories.items():
        logging.info(f"Getting all stories for {category}...")
        category_story_links = get_urls(url, category, params.time_delay)
        logging.info(f"{len(category_story_links)} stories found for {category} category")
        category_urls[category] = category_story_links

    # scrape and write to file
    scrape(params.output_file_name, params.no_of_articles, category_urls, params.time_delay)
