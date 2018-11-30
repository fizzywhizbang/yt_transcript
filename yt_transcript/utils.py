import sys, re

if sys.version_info.major == 3 and sys.version_info.minor >= 4:
    # Python 3.4+
    import html
    html_parser = html
else:
   # Python 3.0 - 3.3
   import html.parser
   html_parser = html.parser.HTMLParser()

def unescape(string):
    return html_parser.unescape(string)

def parse_url(vid_url):
    """
    Take video URL, perform basic sanity check, then filter out video ID.
    @param vid_url: URL of the video to get transcript from.
    @type vid_url: str
    """
    if 'watch?v' in vid_url:
        vid_code = re.findall('^[^=]+=([^&]+)', vid_url)
    elif 'youtu.be/' in vid_url:
        vid_code = re.findall('youtu\.be/([^&]+)', vid_url)
    elif len(vid_url)> 1:
        #assume only code supplied
        return vid_url
    else:
        raise ValueError()
    return vid_code[0]