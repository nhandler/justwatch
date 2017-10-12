#!/usr/bin/env python
import csv

from splinter import Browser
from time import sleep


CONTENT_TYPES = [
    'movie',
    'show',
]

OUTPUT_FILE = "counts.csv"


def get_count(browser):
    titles = browser.find_by_css('.main-content__title-divider')
    count = int(titles.value.split(' ')[0].replace(',', ''))
    return count


def urls_to_rows(browser, urls):
    rows = []
    for url in urls:
        name = url.split('/')[-1]
        for content_type in CONTENT_TYPES:
            browser.visit("{url}?content_type={content_type}".format(url=url, content_type=content_type))
            sleep(1)
            count = get_count(browser)
            row = {
                'provider': name,
                'content_type': content_type,
                'count': count,
            }
            print(row)
            rows.append(row)
    return rows


def rows_to_csv(rows):
    with open(OUTPUT_FILE, "w") as csv_file:
        field_names = ['provider', 'content_type', 'count']
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def get_urls(browser):
    url = "https://www.justwatch.com/us"
    browser.visit(url)
    providers = browser.find_by_css('.provider-filter__wrap.horizontal-scrollable-container').find_by_tag('a')
    urls = []
    for provider in providers:
        href = provider['href']
        urls.append(href)
    return urls


def main():
    with Browser('chrome') as browser:
        urls = get_urls(browser)
        rows = urls_to_rows(browser, urls)
        rows_to_csv(rows)


if __name__ == "__main__":
    main()
