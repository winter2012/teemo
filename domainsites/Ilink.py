# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'bit4'
__github__ = 'https://github.com/bit4woo'

#wydomain
from lib.common import *
from lib.log import logger


class Ilink():
    def __init__(self, domain, proxy=None):
        self.url = 'http://i.links.cn/subdomain/'
        #self.domain = urlparse.urlparse(domain).netloc
        self.domain = domain
        self.subdomains = []
        self.engine_name = "Ilinks"
        self.q = []
        self.timeout = 25
        self.print_banner()
        return

    def print_banner(self):
        logger.info("Searching now in {0}..".format(self.engine_name))
        return

    def run(self):
        try:
            payload = {
                'b2': 1,
                'b3': 1,
                'b4': 1,
                'domain': self.domain
            }
            r = http_request_post(self.url,payload=payload).text
            subs = re.compile(r'(?<=value\=\"http://).*?(?=\"><input)')
            for item in subs.findall(r):
                if is_domain(item):
                    self.q.append(item)

            self.q = list(set(self.q))
        except Exception as e:
            logger.error("Error in {0}: {1}".format(__file__.split('/')[-1],e))
        finally:
            logger.info("{0} found {1} domains".format(self.engine_name, len(self.q)))
            return self.q

if __name__ == "__main__":
    x = Ilink("meizu.com","https://127.0.0.1:9999")
    print x.run()