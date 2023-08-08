import os
import re

def find_urls(htmlString, base_url=None, output=None):
    """ Finds urls in a body of html using regex

    Args:
        htmlString: Html string to extract urls from
        base_url: Baseurl to add to not full urls
        output: Filename for output file (optional)

    Returns: 
        urls: (list of urls)

    """

    # regex: matches urls that are in the href attribute. 
    full_url = re.findall(r'"canonical"(?:.)*?href="(https?://(?:.)*?(?="))', htmlString)

    # regex: matches all url in the href attribute, inside the <a> HTML tag. Ignores fragment identifiers (#). 
    url_regex = r'<a.+?href="([^ ]*?)[#"]'
    urls = re.findall(url_regex, htmlString, re.MULTILINE)
    urls = list(set(urls + full_url))

    if base_url:
        for i, el in enumerate(urls):
            if el.startswith("//"):
                urls[i] = "https:" + el
            if el.startswith("/"):
                urls[i] = base_url + el


    if output:
        path = os.path.join("filter_urls", output + ".txt")
        f = open(path, "w")
        for r in urls:
            f.write(r + "\n")
        f.close()
        return urls

    return urls


def find_articles(htmlString, output=None):
    """ Finds articles calls find_urls and return only urls to Wikipedia articles.
    This function is also using regex and is able to handle any chosen language

    Args:
        htmlString: String of html to extract from
        output: list of articles. "starts with wikipedia"

    Returns: List of articles

    """
    urls = find_urls(htmlString)
    r = re.compile(".*wikipedia")
    articles = list(filter(r.match, urls))
    if output:
        path = os.path.join("filter_urls", output + ".txt")
        f = open(path, "w")
        for r in articles:
            f.write(r + "\n")
        f.close()
        return articles
    return articles

