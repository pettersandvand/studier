from asyncio import events
from fetch_player_statistics import extract_players, extract_teams, extract_player_statistics, make_teamDict, \
    plot_NBA_player_stats
from time_planner import extract_events, create_betting_slip
from filter_urls import find_articles, find_urls
from requesting_urls import get_html


def test_requesting_urls():
    url = "https://en.wikipedia.org/wiki/Studio_Ghibli"
    html_str = get_html(url)
    assert html_str is not None
    html_str = get_html(url, params={"key": " value "})
    assert html_str is not None
    html_str = get_html(url, params={"key": " value "}, output="studio_ghibli")
    assert html_str is not None


def test_requesting_urls_StarWars():
    url = "https://en.wikipedia.org/wiki/Star_Wars"
    html_str = get_html(url)
    assert html_str is not None
    html_str = get_html(url, params={"key": " value "})
    assert html_str is not None
    html_str = get_html(url, params={"key": " value "}, output="star_wars")
    assert html_str is not None


def test_requesting_urls_with_params():
    url = "https://en.wikipedia.org/w/index.php"
    html_str = get_html(url, params={"title": "Main_Page", "action": "info"}, output="main_page", )
    assert html_str is not None


def test_filter_urls_nobel_prize():
    url = "https://en.wikipedia.org/wiki/Nobel_Prize"
    html = get_html(url)
    urls = find_urls(html, output="Nobel_prize_urls", base_url="https://en.wikipedia.org")
    articles = find_articles(html, output="Nobel_prize_articles")
    assert urls is not None
    assert articles is not None


def test_filter_urls_FIS():
    url = "https://en.wikipedia.org/wiki/2019%E2%80%9320_FIS_Alpine_Ski_World_Cup"
    html = get_html(url)
    urls = find_urls(html, output="FIS_urls", base_url="https://en.wikipedia.org")
    articles = find_articles(html, output="FIS_articles")
    assert urls is not None
    assert articles is not None


def test_filter_urls_Bundesliga():
    url = "https://en.wikipedia.org/wiki/Bundesliga"
    html = get_html(url)
    urls = find_urls(html, output="Bundesliga_urls", base_url="https://en.wikipedia.org")
    articles = find_articles(html, output="Bundesliga_articles")
    assert urls is not None
    assert articles is not None


def test_time_planner():
    url = "https://en.wikipedia.org/wiki/2021%E2%80%9322_FIS_Alpine_Ski_World_Cup"
    extract_events(url)
    create_betting_slip(extract_events(url), "betting_slip_empty")


def test_player_statistics_teams():
    nba = "https://en.wikipedia.org/wiki/2021_NBA_playoffs"
    teams = extract_teams(nba)
    assert len(teams[0]) == 8


def test_player_statistics_players():
    players = extract_players("https://en.wikipedia.org/wiki/2020%E2%80%9321_Philadelphia_76ers_season")
    assert len(players[0]) == 17


def test_player_statistics_stats():
    ppg, bpg, rpg = extract_player_statistics("https://en.wikipedia.org/wiki/Ben_Simmons", 2020)
    assert ppg == 14.3
    assert bpg == 0.6
    assert rpg == 7.2

def test_plotting_player_statistics():
    nba = "https://en.wikipedia.org/wiki/2021_NBA_playoffs"
    teams = make_teamDict(nba, 2020)
    plot_NBA_player_stats(teams)
