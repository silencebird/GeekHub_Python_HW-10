import requests
import argparse
import logging
import logging.config
import json
from config import *
import os

if not(os.path.exists('results')):
    os.makedirs('results')


def main():
    dictLogConfig = {
        "version": 1,
        "handlers": {
            "fileHandler": {
                "class": "logging.FileHandler",
                "formatter": "myFormatter",
                "filename": './'+RESULTS+'/'+LOG_FILE
            }
        },
        "loggers": {
            "Parser": {
                "handlers": ["fileHandler"],
                "level": "INFO",
            }
        },
        "formatters": {
            "myFormatter": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            }
        }
    }

    logging.config.dictConfig(dictLogConfig)
    logger = logging.getLogger("Parser")
    logger.info("Program started")

    parser = argparse.ArgumentParser()
    parser.add_argument('--category', default=DEFAULT_CATEGORY, choices=CATEGORIES)
    logger.info("Choose category %s" % parser.parse_args().category)
    payload = {'print': 'pretty'}
    logger.info(REQUEST_URL_CATEGORY + parser.parse_args().category + '.json')

    try:
        response = requests.get(REQUEST_URL_CATEGORY + parser.parse_args().category + '.json',
                            params=payload, timeout=5)

    except:
        print("Oops! Something wrong. Try again...")

    response.encoding = 'UTF-8'
    logger.info("Got request %s" % response.content)
    logger.info("Create a report file %s" % REPORT)


    with open('./'+RESULTS+'/'+REPORT, 'w') as report:
        report.write('by' + '; '+ 'id' + '; '+'score' + '; ' + 'time' + ';' + 'type' + '\n')
        logger.info('Start filter articles(not older - %s; score >= %s)' % (FROM_DATE_DEFAULT, SCORE_DEFAULT))
        for i in (json.loads(response.content)):
            article_text = (requests.get(REQUEST_URL_ARTICLE + str(i) + '.json', params=payload, timeout=5))
            current_article = json.loads(article_text.content)
            if (datetime.datetime.fromtimestamp(current_article['time']) >= FROM_DATE_DEFAULT) and \
                    ((current_article['score']) >= SCORE_DEFAULT):
                logger.info("Write a article with condition")
                print(current_article)
                report.write(str(current_article['by']) + '; ' +\
                             str(current_article['id']) + '; ' +\
                             str(current_article['score']) + '; ' +\
                             str(datetime.datetime.fromtimestamp(current_article['time'])) + ';' +\
                             str(current_article['type']) +
                             '\n')
                print("OK")



    logger.info("Done!")



if __name__ == "__main__":
    main()
