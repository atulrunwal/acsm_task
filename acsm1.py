import requests
import re
import csv


def day(Backpack_value_def):
    day_links = []
    Backpack_value = Backpack_value_def
    session_type_data = ''
    url1 = 'https://www.abstractsonline.com/oe3/Program/9256/Configuration/PP8'
    requests_header1 = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Backpack': Backpack_value,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Host': 'www.abstractsonline.com',
        'Referer': 'https://www.abstractsonline.com/pp8/',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    html_file = requests.get(url1, headers=requests_header1)
    print(html_file.status_code)

    all_links = html_file.json()[42]
    session_type_data1 = all_links['Value'].split('\n')[36].split('@sessiontype=')[1].split('/')[0]
    session_type_data = session_type_data1
    all_day_link = all_links['Value'].split('\n')[6:11]

    for each_split in all_day_link:
        day_link_with_tags = each_split.split('/')[3]
        day_links.append(day_link_with_tags)

        searchid(day_link_with_tags, Backpack_value, session_type_data)


def searchid(day_link_with_tags2, Backpack_value2, session_type_data_passed):
    Backpack_value = Backpack_value2
    day_link_with_tags = day_link_with_tags2
    session_type_data = session_type_data_passed
    url2 = 'https://www.abstractsonline.com/oe3/Program/9256/Search/New/session'

    payload1 = {
        'Phrase': day_link_with_tags
    }

    requests_header2 = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Backpack': Backpack_value,
        'Caller': 'PP8',
        'Connection': 'keep-alive',
        'Content-Length': '28',
        'Content-Type': 'application/json',
        'Host': 'www.abstractsonline.com',
        'Origin': 'https://www.abstractsonline.com',
        'Referer': 'https://www.abstractsonline.com/pp8/',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    html_file2 = requests.post(url2, headers=requests_header2, json=payload1)
    print(html_file2.status_code)
    searchid_json = html_file2.json()
    searchid = searchid_json['SearchId']
    id(searchid, Backpack_value, session_type_data)


def id(searchid1, Backpack_value3, session_type_data_passed):
    searchid = searchid1
    Backpack_value = Backpack_value3
    session_type_data = session_type_data_passed

    url_for_resultspage = f'https://www.abstractsonline.com/oe3/Program/9256/Search/{searchid}/Results?'

    payload2 = {
        'page': '1',
        'pagesize': '',
        'total_pages': '0',
        'sort': '1',
        'order': 'asc'
    }
    requests_header3 = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Backpack': Backpack_value,
        'Connection': 'keep-alive',
        'Host': 'www.abstractsonline.com',
        'Referer': 'https://www.abstractsonline.com/pp8/',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    all_id = []
    html_file3 = requests.get(url_for_resultspage, headers=requests_header3, json=payload2)
    print(html_file3.status_code)
    id = html_file3.json()

    for i in id['Results']:
        ids = i['Id']
        print(ids)
        all_id.append(ids)
        author(Backpack_value, ids, session_type_data)


def author(Backpack_value4, ids1, session_type_data_passed):
    Backpack_value = Backpack_value4
    ids = ids1
    session_type_data_from_author = session_type_data_passed

    f = open('acsm_task.csv', 'a', newline='')
    csv_writer = csv.writer(f)

    url_for_author = f'https://www.abstractsonline.com/oe3/Program/9256/Session/{ids}'

    author_url_to_print = 'https://www.abstractsonline.com/pp8/#!/9256/session/'

    requests_header4 = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Backpack': Backpack_value,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Host': 'www.abstractsonline.com',
        'Referer': 'https://www.abstractsonline.com/pp8/',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    html_file4 = requests.get(url_for_author, headers=requests_header4)
    print(html_file4.status_code)
    author = html_file4.json()

    authors = None
    authoraffilation_clean_text = None
    abstract_clean_text = None
    location = None
    session_type_data = None
    catagory_for_presentation = None
    sub_category = None
    discloser_clean_text = None
    print('=' * 30)
    print('Autor data')
    print('=' * 30)

    date = author['Date']
    print('Date : ', date)

    start_time = author['StartTime']
    print('Start Time : ', start_time)

    end_time = author['EndTime']
    print('Ent Time : ', end_time)

    article_title = author['SearchResultBody']
    print('Article Title : ', article_title)

    session_title_author = article_title
    print('Session title : ', session_title_author)

    url_author = author_url_to_print + ids
    print('url : ', url_author)

    csv_writer.writerow(
        [article_title, url_author, authors, authoraffilation_clean_text, abstract_clean_text, date,
         start_time, end_time,
         location, session_title_author, session_type_data, catagory_for_presentation, sub_category,
         discloser_clean_text])
    f.close()

    catagory_for_presentation_from_author = author['PrimaryCategory']
    presentations(Backpack_value, ids, catagory_for_presentation_from_author, session_type_data_from_author)


def presentations(Backpack_value5, ids2, catagory_for_presentation1, session_type_data_passed):
    Backpack_value = Backpack_value5
    ids = ids2
    catagory_for_presentation = catagory_for_presentation1
    session_type_data = session_type_data_passed

    f = open('acsm_task.csv', 'a', newline='')
    csv_writer = csv.writer(f)

    url_for_presentation = f'https://www.abstractsonline.com/oe3/Program/9256/Session/{ids}/presentations'
    presentation_url_to_print_ = 'https://www.abstractsonline.com/pp8/#!/9256/presentation/'

    requests_header5 = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Backpack': Backpack_value,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Host': 'www.abstractsonline.com',
        'Referer': 'https://www.abstractsonline.com/pp8/',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    html_file5 = requests.get(url_for_presentation, headers=requests_header5)
    print(html_file5.status_code)
    presentation_info = html_file5.json()

    print('=' * 30)
    print('Presentations')
    print('=' * 30)

    location = None
    sub_category = None

    for abstract in presentation_info:
        try:

            presentation_url_id = abstract['Id']
            url_presentation = presentation_url_to_print_ + presentation_url_id
            print('Url : ', url_presentation)
            abstracts_with_tags = abstract['Abstract']

            abstract_cleaner = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
            abstract_clean_text = re.sub(abstract_cleaner, '', abstracts_with_tags)
            print('Abstract : ', abstract_clean_text)

            authors_with_authoraffiliation = abstract['AuthorBlock']
            authors_only = authors_with_authoraffiliation.split('<I>')
            authors = authors_only[0]
            print('Authors : ', authors)

            authorsaffilation_with_tags = authors_only[1]
            authoraffilation_cleaner = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
            authoraffilation_clean_text = re.sub(authoraffilation_cleaner, '', authorsaffilation_with_tags)
            print('Authors Affilation : ', authoraffilation_clean_text)

            article_title_with_tags = abstract['Title']
            article_title_cleaner = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
            article_title_clean_text = re.sub(article_title_cleaner, '', article_title_with_tags)
            print('Article_title : ', article_title_clean_text)

            date_with_time = abstract['Start']
            end_time_with_date = abstract['End']
            date_with_time_split = date_with_time.split(' ')
            end_time_with_date_split = end_time_with_date.split(' ')
            date = date_with_time_split[0]
            start_time = date_with_time_split[1]
            end_time = end_time_with_date_split[1]

            print('Date  : ', date)
            print('Start time : ', start_time)
            print('End time : ', end_time)

            session_title = article_title_clean_text
            print(session_title)

            print('Session type : ', session_type_data)

            print('catagory : ', catagory_for_presentation)

            discloser_with_tags = abstract['DisclosureBlock']
            discloser_cleaner = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
            discloser_clean_text = re.sub(discloser_cleaner, '', discloser_with_tags)
            print('Discloser : ', discloser_clean_text)

            print('-' * 50)

            csv_writer.writerow(
                [article_title_clean_text, url_presentation, authors, authoraffilation_clean_text, abstract_clean_text,
                 date, start_time, end_time,
                 location, session_title, session_type_data, catagory_for_presentation, sub_category,
                 discloser_clean_text])

        except Exception as e:
            print(e)
    f.close()


def main():
    f = open('acsm_task.csv', 'w', newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(
        ['article_title', 'url', 'authors', 'author_affiliation', 'abstract_text', 'date', 'start_time', 'end_time',
         'location', 'session_title', 'session_type', 'category', 'sub_category', 'disclosure'])
    f.close()
    Backpack_value = 'e993c19b-25e6-419c-a5d0-b2a6c6bda656'
    day(Backpack_value)


main()
