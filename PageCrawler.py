import sys
import os
from termcolor import colored
from src.crawler import Crawler, CrawlerRequest

if len(sys.argv) < 2:
    print(colored('Please provide the input file as argument.', 'yellow'),
          colored('For eg:', 'yellow'))
    print(colored('$ python AMPCrawler.py /path/to/your/file.txt', 'green'))
    sys.exit(1)
elif (not os.path.exists(sys.argv[1]) and
      not os.path.isfile(sys.argv[1])):
    print(colored('Make sure given file is on correct path', 'red'),
          colored('and file type is file', 'red'))
    sys.exit(1)

try:
    file = sys.argv[1]
    ampCrawl = Crawler(file)
    ampCrawl.run_crawler()
    ampCrawl.show_result()

    sys.exit(ampCrawl.exit_code())
except Exception as e:
    print("Crawler script failing with error:\n%s" % (e))
    sys.exit(1)
