import urllib.request


class FileChecker():
    def check_file(self, file_url):
        try:
            urllib.request.urlopen(file_url, timeout=5).getcode()
        except:
            print('404 at:', file_url)