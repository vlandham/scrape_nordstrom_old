# -*- coding: utf-8 -*-

# Scrapy settings for scrape_nordstrom project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrape_nordstrom'

SPIDER_MODULES = ['scrape_nordstrom.spiders']
NEWSPIDER_MODULE = 'scrape_nordstrom.spiders'
DUPEFILTER_CLASS = 'scrape_nordstrom.custom_filters.SeenURLFilter'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrape_nordstrom (+http://www.yourdomain.com)'
