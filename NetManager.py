import urllib.request
import urllib.parse
import http.cookiejar


class NetManager:
    def __init__(self):
        cj = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(
            urllib.request.HTTPCookieProcessor(cj))

    def get(self, url, data=None, encoding='utf-8'):
        # request = urllib.request.Request(url, data.encode())
        request = urllib.request.Request(url)
        if encoding == 'raw':
            return self.opener.open(request, timeout=15).read()
            # return urllib.request.urlopen(request).read()
        else:
            return self.opener.open(request, timeout=15).read().decode(encoding)
            # return urllib.request.urlopen(request).read().decode(encoding)

    def post(self, url, data=None, encoding='utf-8'):
        request = urllib.request.Request(
            url, urllib.parse.urlencode(data).encode())
        if encoding == 'raw':
            return self.opener.open(request, timeout=15).read()
            # return urllib.request.urlopen(request).read()
        else:
            return self.opener.open(request, timeout=15).read().decode(encoding)
            # return urllib.request.urlopen(request).read().decode(encoding)
