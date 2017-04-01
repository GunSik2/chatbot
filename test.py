import goslate
import urllib.request

proxy = urllib.request.ProxyHandler({'http': '127.0.0.1:5000'})
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)

# urllib.request.urlretrieve('http://www.google.com')
#
#
# proxy_handler = urllib.request.ProxyHandler({'http' : 'http://cee59643.ngrok.io'})
# proxy_opener = urllib.request.build_opener(urllib.request.HTTPHandler(proxy_handler),
#                                     urllib.request.HTTPSHandler(proxy_handler))

gs_with_proxy = goslate.Goslate(opener=opener)
translation = gs_with_proxy.translate("hello world", "de")

print(translation)
