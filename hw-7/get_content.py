import requests
import re
from bs4 import BeautifulSoup as bs


def get_content(lang):
    response = requests.get('https://www.flpkgz.com/faq/kg/' + lang + '/')
    sections_from_html = bs(response.content.decode('utf-8'), 'html.parser')

    # Parse words for section buttons
    section_list = []
    for section in sections_from_html.select('.alert'):
        section_list.append(section.text.strip())

    # Parse words for subsection buttons and data
    subsection_list = []
    for subsection in sections_from_html.find_all('h3', {'itemprop': 'name'}):
        subsection = re.sub(r"\s+", " ", subsection.text, flags=re.UNICODE).strip()
        subsection_list.append(subsection)

    questions = sections_from_html.find_all(
        'div', {'itemtype': 'https://schema.org/Question'})
    answers = [
        [re.sub(r"\s+", " ", (getattr(i.find('h3', {'itemprop': 'name'}), 'text', 'N/A')), flags=re.UNICODE).strip(),
         re.sub(r"\s+", " ", (getattr(i.find('div', {'itemprop': 'acceptedAnswer'}), 'text', 'N/A')),
                flags=re.UNICODE).strip(),
         i.find_all('img')
         ] for i in questions]
    return section_list, subsection_list, questions, answers
