 # import the module
import os

import requests as req


def get_html(url, params=None, output=None):
    """
    Get html from a url
    Args:
        url: url to page to convert to string
        params: other params to use in the parsing
        output: if you want to save the output to a file, add filename

    Returns: String of html from page.

    """
    #passing the optional arguments to the get function
    res = req.get(url, params = params)
    response = str(res.text)
    if output:
        path = os.path.join("requesting_url", output + ".txt")
        f = open(path,  "w")
        f.write(response)
        f.close()
        return res
    return response



