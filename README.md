# Python Page Crawler

`PageCrawler` was written in order to provide easier integration with jenkins as part of application deployment checks.
It is written in Python and provides an easy way to check list of url in a file and showing the http status code of the given page. If it found there are pages showing http status code >= 400 (which includes 404, 500, 403 etc), it will finish the script with exit code 1 and will trigger jenkins build to fail.

## Quickstart
Run the script with:

```shell
$ python PageCrawler.py urls.txt
HTTP Status ✅ is 200 http://www.example.com/
Success: 1
Failed: 0
```

## Note
This is written on python 3.7. So i haven't tested it yet on python <= 3.7. So use on your own risk and update as required.