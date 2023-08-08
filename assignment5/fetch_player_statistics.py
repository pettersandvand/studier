import re
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
import random
from filter_urls import find_urls
from requesting_urls import get_html


def extract_teams(url):
    """Extract team names and urls from the NBA Playoff 'Bracket' section table.

    Returns:
        team_names (list): A list of team names that made it to the conference
            semifinals.
        team_urls (list): A list of absolute Wikipedia urls corresponding to team_names.

    """
    # get html using for example get_html from requesting_urls
    html = get_html(url)

    # create soup
    soup = BeautifulSoup(html, "html.parser")
    # find bracket we are interested in
    bracket_header = soup.find(id="Bracket")
    bracket_table = bracket_header.find_next("table")
    rows = bracket_table.find_all("tr")

    links = [a for a in [r.find("a") for r in rows] if a]
    team_names = [el.text for el in links]
    results = {name:
                   team_names.count(name)
               for name in team_names}
    teams = {link.text:
                 find_urls(str(link), base_url="https://en.wikipedia.org")[0]
             for link in links}
    # remove links to conferences
    teams.pop("Eastern Conference")
    teams.pop("Western Conference")
    teams.pop("First Round")

    # create lists of team names and urls to the team website
    team_names = []
    team_urls = []
    for key in teams:
        if results[key] > 1:
            team_names.append(key)
            team_urls.append(teams[key])

    return team_names, team_urls


def extract_players(team_url):
    """Extract players that played for a specific team in the NBA playoffs.

    Args:
        team_url (str): URL to the Wikipedia article of the season of a given
            team.

    Returns:
        player_names (list): A list of players names corresponding to the team whos URL was passed.
            semifinals.
        player_urls (list): A list of Wikipedia URLs corresponding to
            player_names of the team whos URL was passed.

    """

    # keep base url
    base_url = "https://en.wikipedia.org"

    # get html for each page using the team url you extracted before
    html = get_html(team_url)

    # make soup
    soup = BeautifulSoup(html, "html.parser")
    # get the header of the Roster
    roster_header = soup.find(id="Roster")
    # identify table
    roster_table = roster_header.find_next("table")
    rows = roster_table.find_all("tr")

    # prepare lists for player names and urls
    player_names = []
    player_urls = []

    for i in range(0, len(rows)):
        cells = rows[i].find_all("td")
        cells_text = [cell.get_text(strip=True) for cell in cells]
        player_name = None
        player_url = None
        if len(cells_text) == 7:
            rel_url = cells[2].find_next("a")
            player_url = (extract_url(rel_url, base_url=base_url))
            if 2 < len(cells):
                # regex: find player name in cell
                player_name_regex = re.findall("([A-Z][a-z]*)[\s-]([A-Z][a-z]*)", str(cells[2].find_next("a")))
                if len(player_name_regex) > 0:
                    player_name = (player_name_regex[0][0] + ' ' + player_name_regex[0][1])
                # create urls to each player
                # need to create absolute urls combining the base and the relative url
        if player_name is not None and player_url is not None:
            player_urls.append(player_url)
            player_names.append(player_name)
    return player_names, player_urls


def extract_url(html, base_url=None):
    """

    Args:
        html: html string
        base_url: if there are links with / the base url will be added to the start

    Returns: string of url

    """
    url = html.attrs["href"]

    if base_url:
        if url.startswith("/"):
            url = base_url + url
    return url


def extract_player_statistics(player_url, year):
    """Extract player statistics for NBA player.

    # Note: Make yourself familiar with the 2020-2021 player statistics wikipedia page and adapt the code accordingly.

    Args:
        player_url (str): URL to the Wikipedia article of a player.
        year (int): start year of the season you want stats from.

    Returns:
        ppg (float): Points per Game.
        bpg (float): Blocks per Game.
        rpg (float): Rebounds per Game.

    """
    # default score for players have incomplete statistics/information
    ppg = 0.0
    bpg = 0.0
    rpg = 0.0

    html = get_html(player_url)
    soup = BeautifulSoup(html, "html.parser")

    # find header of NBA career statistics
    nba_header = soup.find(id="NBA_career_statistics")

    # check for alternative name of header
    if nba_header is None:
        nba_header = soup.find(id="NBA")

    try:
        # find regular season header
        # You might want to check for different spellings, e.g. capitalization
        # You also want to take into account the different orders of header and table
        regular_season_header = nba_header.find_next(id="Regular_season")

        # next we should identify the table
        nba_table = regular_season_header.find_next("table")

    except:
        try:
            # table might be right after NBA career statistics header
            nba_table = nba_header.find_next("table")

        except:
            return ppg, bpg, rpg

    # find nba table header and extract rows
    headings = []
    for td in nba_table.find_all("th"):
        # remove any newlines and extra spaces from left and right
        headings.append(td.text.replace('\\n', '').strip())

    for tr in nba_table.tbody.find_all("tr"):  # find all tr's from table's tbody
        # Each table row is stored in the form of
        # find all td's(3) in tr and zip it with t_header

        if str(year) in tr.text:
            for td, th in zip(tr.find_all("td"), headings):
                if th == "PPG":
                    ppg = float(td.text.replace('\\n', '').replace("*", "").strip())
                if th == "BPG":
                    bpg = float(td.text.replace('\\n', '').replace("*", "").strip())
                if th == "RPG":
                    rpg = float(td.text.replace('\\n', '').replace("*", "").strip())

    # Convert the scores extracted to floats Note: In some cases the scores are not defined but only shown as '-'. In
    # such cases you can just set the score to zero or not defined.

    return ppg, bpg, rpg


def make_teamDict(url, year):
    """
    Main function to extract teams form a url
    Args:
        url (str): URL to the Wikipedia article of season.
        year (int): start year of the season you want stats from.
    Returns: Dict of teams on style:
                            "Team name" : [
                            {
                                "playerName" :
                                "ppg":
                                "bpg":
                                "rpg":
                            },
                            ...
                        ]
                            ...

    """
    teams = extract_teams(url)
    teamDict = {}

    teamNames = teams[0]
    teamUrls = teams[1]
    for i in range(len(teamUrls)):
        teamName = teamNames[i]
        teamUrl = teamUrls[i]
        players = extract_players(teamUrl)
        playerList = []
        playerNames = players[0]
        playerUrls = players[1]
        for j in range(len(playerUrls)):
            playerName = playerNames[j]
            playerUrl = playerUrls[j]
            stats = extract_player_statistics(playerUrl, year)
            ppg = stats[0]
            bpg = stats[1]
            rpg = stats[2]
            pDict = {
                "name": playerName,
                "ppg": ppg,
                "bpg": bpg,
                "rpg": rpg,
            }
            playerList.append(pDict)
        sortedPlayers = sorted(playerList, key=lambda d: d["ppg"], reverse=True)

        teamDict[teamName] = sortedPlayers[:3]

    return teamDict


def make_plot(teams, statsType):
    """

    Args:
        teams: Dict of teams
        statsType (str): Type of stats you want. {"ppg", "bpg", "rpg"}

    Returns:

    """
    count_so_far = 0
    all_names = []
    plt.cla()
    for team, players in teams.items():
        r = random.random()
        b = random.random()
        g = random.random()
        color = (r, g, b)
        val = []
        names = []
        for player in players:
            names.append(player["name"])
            val.append(player[statsType])
        all_names.extend(names)

        x = range(count_so_far, count_so_far + len(players))
        count_so_far += len(players)
        bars = plt.bar(x, val, color=color, label=team)
        plt.bar_label(bars)
    plt.xticks(range(len(all_names)), all_names, rotation=90)

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
               fancybox=True, shadow=True, ncol=8)
    plt.grid(False)
    if statsType == "ppg":
        plt.title("points per game", y=1.3)
    elif statsType == "bpg":
        plt.title("Blocks per Game", y=1.3)
    elif statsType == "rpg":
        plt.title("Rebounds per Game", y=1.3)
    else:
        plt.title("Unknown", y=1.3)
    plt.savefig("NBA_player_statistics/players_over_" + statsType + ".png", bbox_inches="tight")


def plot_NBA_player_stats(teams):
    """

    Args:
        teams: Dictonary of teamses on this style
            "Teamname" : [
                            {
                                "playerName" :
                                "ppg":
                                "bpg":
                                "rpg":
                            },
                            ...
                        ]
            ...

    Returns: Makes plotfiles in NBA_player_statistics folder

    """
    make_plot(teams, "ppg")
    make_plot(teams, "bpg")
    make_plot(teams, "rpg")
