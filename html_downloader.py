import urllib2

class HtmlDownloader(object):
	"""docstring for HtmlDownLoader"""
 	def download(self,url):
 	 	if url is None:
 	 		return None

 	 	response = urllib2.urlopen(url)
 	 	if response.getcode() != 200:
 	 		return None

 	 	return response.read()


 