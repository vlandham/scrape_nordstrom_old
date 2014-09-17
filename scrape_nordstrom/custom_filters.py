from scrapy.dupefilter import RFPDupeFilter

class SeenURLFilter(RFPDupeFilter):
  """A dupe filter that considers the URL"""

  def __init__(self, path=None, debug=False):
    self.urls_seen = set()
    RFPDupeFilter.__init__(self, path, debug)

  def get_id(self, url):
    return url.split("?")[0]

  def request_seen(self, request):
    url = self.get_id(request.url)
    if url in self.urls_seen:
      return True
    else:
      self.urls_seen.add(url)
    return False
