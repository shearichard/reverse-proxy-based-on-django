from revproxy.views import ProxyView

class TestProxyView(ProxyView):
    #upstream = 'http://example.com'
    upstream = 'http://127.0.0.1:5000'
