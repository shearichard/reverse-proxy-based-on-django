from revproxy.views import ProxyView

class TestProxyView(ProxyView):
    upstream = 'http://example.com'
