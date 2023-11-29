from typing import Tuple, List
import lxml.html as html


def scrape_from_html(html: html) -> Tuple[List, List]:
    """
    Function that takes html from a quizlet page and converts it to a tuple of two lists, fronts and backs
    html : lxml.html object that is the current page the user is visiting

    Returns a tuple ([list of card fronts], [List of card backs])
    """
    elements = html.xpath("//span[@class='TermText']")
    fronts = []
    backs = []
    for count, element in enumerate(elements):
        if count % 2 == 0:
            fronts.append(element.text_content())
            continue
        backs.append(elements.text)
    return (fronts, backs)
