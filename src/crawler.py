import requests
from termcolor import colored


class CrawlerRequest(object):
    """
    Crawler request params. Will return following params:
    - self.status_code
    - self.url
    - self.history_status_code
    - self.history_url
    """
    def __init__(self, request):
        self._req = request
        self.status_code = self._req.status_code
        self.url = self._req.url

        if self._req.history != []:
            self.history_status_code = self._req.history[0].status_code
            self.history_url = self._req.history[0].url
        else:
            self.history_status_code = self.status_code
            self.history_url = self.url


class Crawler(object):
    """Crawler client

    Attributes:
        file (str): Path to file containing list of urls to crawl.
    """
    def __init__(self, file):
        self.success_count = 0
        self.failed_count = 0
        self.file = file

    def get_mark(self):
        white_check_mark = '\u2705'
        cross_mark = '\u274c'

        if self.request.status_code >= 400:
            return cross_mark
        else:
            return white_check_mark

    def run_crawler(self):
        file = open(self.file, 'r')
        list = file.read().splitlines()

        for url in list:
            self.request = CrawlerRequest(requests.get(url))
            if self.request.status_code >= 400:
                retry = 1
                while retry <= 5 and self.request.status_code >= 400:
                    print('retry %d for %s' %(retry, self.request.url))
                    self.request = CrawlerRequest(requests.get(url))
                    retry = retry + 1
            self.update_count()
            self.show_status()

    def update_count(self):
        if self.request.status_code == 200:
            self.success_count += 1
        elif self.request.status_code >= 400:
            self.failed_count += 1

    def show_status(self):
        message = "HTTP Status %s is %d" % (
            self.get_mark(),
            self.request.status_code
        )

        if (
            self.request.history_status_code == 200 or
            self.request.history_status_code >= 400
           ):
                message = message + ' ' + self.request.url
        elif (
            self.request.history_status_code == 301 or
            self.request.history_status_code == 302
           ):
                message = (message +
                           ' ' +
                           "after %s redirect from %s to %s" % (
                                self.history_status_code,
                                self.request.history_url,
                                self.request.url)
                            )
        print(message)

    def show_result(self):
        success = colored('Success: %d', 'green') % (self.success_count)
        failed = colored('Failed: %d', 'red') % (self.failed_count)
        print("%s\n%s" % (success, failed))

    def exit_code(self):
        if self.failed_count > 0:
            exit_code = 1
        else:
            exit_code = 0

        return exit_code