import requests
import argparse
import logging
import logging.config
import datetime
import time
import json
import pickle
import os
import re
from config import *
from jinja2 import Environment, FileSystemLoader
import psycopg2
import psycopg2.extras


if not(os.path.exists('results')):
    os.makedirs('results')

tag = re.compile(r'<.*s?>')

class Logger(object):

    def __init__(self, config):
        self.init_logger(config)
        self.logger = logging.getLogger("Parser")
        self.lvls = {
            'critical': 50,
            'error': 40,
            'warning': 30,
            'info': 20,
            'debug': 10,
            'notset': 0
        }

    def init_logger(self, config):
        logging.config.dictConfig(config)

    def write_log(self, log_type, message):
        self.logger.log(self.lvls[log_type], message)


class Argparse(object):

    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def add_args(self, default, choices):
        self.parser.add_argument('--category', default=default, choices=choices)

    def get_args(self, choices):
        if self.parser.parse_args().category == 'all':
            return choices[:-1]
        else:
            return self.parser.parse_args().category



class Parser(object):

    def __init__(self):
        self.response = ''

    def parse_data(self, url, params, timeout):
        self.response = requests.get(url, params=params, timeout=timeout)

    def encode_response(self, text_format):
        self.response.encoding = text_format

    def get_resonse_content(self):
        return json.loads(self.response.content)


class Archive(object):

    def __init__(self, file_name):
        self.file_name = file_name
        self.article_list = {}

    def clear_article_list(self):
        self.article_list = {}

    def save_data(self, data):
        output = open('{}.pkl'.format(self.file_name), 'wb')
        pickle.dump(data, output)
        output.close()

    def load_data(self):
        pkl_file = open('{}.pkl'.format(self.file_name), 'rb')
        data = pickle.load(pkl_file)
        pkl_file.close()
        return data

    def update_archive(self, data):
        if not(os.path.isfile('{}.pkl'.format(self.file_name))):
            self.save_data(data)
            return data
        else:
            new_data = self.data_compare(data)
            archive_data = self.load_data()
            self.save_data(archive_data + new_data)
            return new_data

    def data_compare(self, data):
        archive_data = self.load_data()
        new_data = list(set(data) - set(archive_data))
        return new_data


class HTMLCreator(object):

    def render_template(self, template_filename, template_folder, context):
        path = os.path.dirname(os.path.abspath(__file__))
        template_environment = Environment(
            autoescape=False,
            loader=FileSystemLoader(os.path.join(path, '{}'.format(template_folder))),
            trim_blocks=False)
        return template_environment.get_template(template_filename).render(context)

    def create_html_file(self, output_file_name, template_file, template_folder, data):
        output_file = '{}.html'.format(output_file_name)
        context = {
            'articles': data
        }
        with open(output_file, 'w', encoding="utf-8") as f:
            html = self.render_template('{}.html'.format(template_file), template_folder, context)
            f.write(html)


class Article(object):

    def __init__(self, filter_pattern):
        self.filter_pattern = filter_pattern
        self.article_content = dict.fromkeys([
           "id", "by", "deleted", "text", "dead", "parent", "descendants", "kids",
           "score", "time", "title", "type", "url", "parts", "poll"
        ])

    def update_content(self, article_data):
        for key, value in article_data.items():
            if key == 'text':
                self.article_content[key] = self.filter_pattern.sub('', value)
            elif key == 'time':
                self.article_content[key] = datetime.datetime.fromtimestamp(value)
            else:
                self.article_content[key] = value


class DataBase(object):
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                "dbname='HackerNews' user='postgres' host='localhost' password='nester1987' port='5432'")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        except ValueError:
            print('Oops! Something wrong. Try again...{}'.format(ValueError))

    def create_table(self, table_name):
        create_table_command = ("""CREATE TABLE {} (
                                        id integer PRIMARY KEY, 
                                        by text, 
                                        deleted bool,
                                        text text,
                                        dead bool,
                                        parent text,
                                        descendants integer ,
                                        kids integer[],
                                        score integer,
                                        time timestamp,
                                        title text,
                                        type text,
                                        url text,
                                        parts integer[],
                                        poll integer);""".format(table_name))
        self.cursor.execute(create_table_command)

    def exist_table_check(self, table_name):
        self.cursor.execute("""SELECT EXISTS (
                                                  SELECT 1 
                                                  FROM   pg_tables
                                                  WHERE  schemaname = 'public'
                                                  AND    tablename = %s
                                                  );""", (table_name,))
        return self.cursor.fetchone()['exists']

    def write_to_db(self, table_name, data):
        self.cursor.execute("SELECT id FROM {};".format(table_name))
        db_ids = [d['id'] for d in self.cursor.fetchall()]
        data_id = data['id']
        if not (data_id in db_ids):
            self.insert_data(table_name, data)
        else:
            self.update_table(table_name, data)

    def insert_data(self, table_name, data):
        cols = ",".join(data.keys())
        psycopg_marks = ','.join(['%s' for s in data.keys()])
        values = [v for v in data.values()]
        insert_statement = "INSERT INTO {} ({}) VALUES ({});".format(table_name, cols, psycopg_marks)
        self.cursor.execute(insert_statement, values,)

    def update_table(self, table_name, data):
        for key, value in data.items():
            update_statement = "UPDATE {} SET {}=%s WHERE id = %s;".format(table_name, key)
            if key != 'id':
                self.cursor.execute(update_statement, (value, str(data['id'],)))

    def query_all(self, table_name):
        self.cursor.execute("SELECT * FROM {};".format(table_name))
        return self.cursor.fetchall()

    def drop_table(self, name):
        update_command = "DROP TABLE {};".format(name)
        self.cursor.execute(update_command)

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

if __name__ == "__main__":
    archive = Archive(ARCHIVE_FILENAME)
    archive.clear_article_list()
    database = DataBase()
    html_creator = HTMLCreator()
    logger = Logger(DICT_LOG_CONFIG)
    logger.write_log('info', "Program started")
    args_parser = Argparse()
    args_parser.add_args(DEFAULT_CATEGORY, CATEGORIES)
    logger.write_log('info', 'Choose category {}'.format(args_parser.get_args(CATEGORIES)))
    logger.write_log('info', 'Get data from: {}{}.json'.format(REQUEST_URL_CATEGORY, args_parser.get_args(CATEGORIES)))
    categories = args_parser.get_args(CATEGORIES)
    if not(type(categories) is tuple):
        categories =[categories]
    parser = Parser()
    for category in categories:
        if not database.exist_table_check(category):
            database.create_table(category)
        try:
            parser.parse_data('{}{}.json'.format(REQUEST_URL_CATEGORY, category), PAYLOAD, 5)
        except ValueError:
            print('Oops! Something wrong. Try again...{}'.format(ValueError))
            logger.write_log('error', 'Request error {}'.format(ValueError))

        parser.encode_response('UTF-8')
        articles_ids = parser.get_resonse_content()
        articles_ids = archive.update_archive(articles_ids)
        for article_id in articles_ids:
            try:
                parser.parse_data('{}{}.json'.format(REQUEST_URL_ARTICLE, article_id), PAYLOAD, 5)
            except ValueError:
                print('Oops! Something wrong. Try again...{}'.format(ValueError))
                logger.write_log('error', 'Request error {}'.format(ValueError))
            current_article = parser.get_resonse_content()
            if current_article:
                if datetime.datetime.fromtimestamp(current_article['time']) >= FROM_DATE_DEFAULT:
                    if (current_article['score']) >= SCORE_DEFAULT:
                        parser.encode_response('UTF-8')
                        article = Article(tag)
                        article.update_content(current_article)
                        logger.write_log('info', 'Write article to database {}'.format(current_article['title']))
                        database.write_to_db(category, article.article_content)
        archive.article_list[category] = database.query_all(category)


    html_creator.create_html_file(
        time.strftime("%Y%m%d-%H%M%S"), 'template', 'templates', archive.article_list
    )
    database.close_connection()

