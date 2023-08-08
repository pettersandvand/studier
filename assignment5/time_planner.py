import os
import re
from bs4 import BeautifulSoup

from requesting_urls import get_html

def extract_events(url):
    """ Extract date , venue and discipline for competitions .
    
    Args :
        url (str): The url to extract events from .
    Returns :
        table_info ( list of lists ): A nested list where the rows represent each race date , 
        and the columns are [date , venue ,discipline ].
    """

    html = get_html(url)
    # make soup
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find('table', {"class": "wikitable"})
    table_rows = table.find_all("tr")

    # display tables
    for i in table_rows:
        table_data = i.find_all('td')

    headings = []
    for td in table.find_all("th"):
        # remove any newlines and extra spaces from left and right
        headings.append(td.text.replace('\\n', '').strip())


    table_data = []
    venueSpanNr = 0
    venueSpanContent = None
    slopeSpanNr = 0
    slopeSpanContent = None
    for tr in table.tbody.find_all("tr"):  # find all tr's from table's tbody
        t_row = {}
        # Each table row is stored in the form of
        # find all td's(3) in tr and zip it with t_header
        for td, th in zip(tr.find_all("td"), headings):

            if th == "Venue" or th == "Slope (incline)":
                if venueSpanNr == 0 and th == "Venue":
                    if td.has_attr('rowspan'):
                        venueSpanNr = int(td.attrs["rowspan"])
                        venueSpanContent = td.text.replace('\n', '').strip()

                    t_row[th] = td.text.replace('\n', '').strip()

                if slopeSpanNr == 0 and th == "Slope (incline)":
                    if td.has_attr('rowspan'):
                        slopeSpanNr = int(td.attrs["rowspan"])
                        slopeSpanContent = td.text.replace('\n', '').strip()

                    t_row[th] = td.text.replace('\n', '').strip()
                if venueSpanNr > 0 and th == "Venue":
                    t_row[th] = venueSpanContent
                    venueSpanNr = venueSpanNr - 1

                if slopeSpanNr > 0 and th == "Slope (incline)":
                    t_row[th] = slopeSpanContent
                    slopeSpanNr = slopeSpanNr - 1

            else:
                t_row[th] = td.text.replace('\n', '').strip()
        #adding type, because of the rowspan this way of dooing it jumps over it.
        for disipline in re.findall("\D[A-Z] \d\d\d", tr.text):
            t_row["Type"] = disipline
        if not len(t_row) < 3:
            table_data.append(t_row)

    events = []

    disciplines = {
        "DH": "Downhill",
        "SL": "Slalom",
        "GS": "Giant Slalom",
        "SG": "Super Giant Slalom",
        "AC": "Alpine Combined",
        "PG": "Parallel Giant Slalom ",
    }
    for d in table_data:
        date = d["Date"]
        venue = d["Venue"] 
        t = d["Type"]
        disipline = t.split()
        disipline = disciplines[disipline[0]]
        events.append((date, venue, disipline))

    return events

def create_betting_slip(events, save_as):
    """

    Args:
        events: Events to make bettning slipp from
        save_as: filename

    Returns: None

    """
    dir = "datetime_filter"
    # save_as = 'betting_slip_empty.md'
    os.makedirs(dir, exist_ok=True)

    with open(f"./{dir}/{save_as}.md", "w") as f:
        f.write(f"# BETTING SLIP ({save_as})\n\nName:\n\n")
        f.write("Date | Venue | Discipline | Who wins?\n")
        f.write(" --- | --- | --- | --- \n")
        for e in events:
            dates, venue, discipline = e
            f.write(f"{dates} | {venue} | {discipline}|\n")
        
    


