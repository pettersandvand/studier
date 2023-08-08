from typing import Optional
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from webvisualization_plots import plot_reported_cases_per_million, all_countries

# create app variable (FastAPI instance)
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# mount one or more static directories,
# e.g. your auto-generated Sphinx documentation with html files
app.mount(
    # the URL where these files will be available
    "/help",
    StaticFiles(
        # the directory the files are in
        directory="docs\\_build\\html\\",
        html=True,
    ),
    # an internal name for FastAPI
    name="static",
)


@app.get("/")
def plot_reported_cases_per_million_html(request: Request):
    """
    Root route for the web application.
    Handle requests that go to the path "/".

    Args:
        request: API reqest

    Returns: Main page

    """

    return templates.TemplateResponse(
        "plot_reported_cases_per_million.html",
        {
            "request": request,
            # further template inputs here
            "country": all_countries(),
        },
    )


@app.get("/plot_reported_cases_per_million.json")
def plot_reported_cases_per_million_json(countries: Optional[str] = None,
                                         start: Optional[str] = None,
                                         end: Optional[str] = None):
    """
    Handles routes that direct for '/plot_reported_cases_per_million.json'
    Function to get a custom chart.

    Args:
        countries (list(string)): List of countries to be included in the plot.
        start (string, optional): The first date to include in the returned dataframe.
            If specified, records earlier than this will be excluded.
            Default: include earliest date
            Example format: "2021-10-10"
        end (string, optional): The latest date to include in the returned data frame.
            If specified, records later than this will be excluded.
            Example format: "2021-10-10"

    Returns:
         altair Chart of number of reported covid-19 cases over time.

    """
    if countries:
        countries = countries.split(",")
    else:
        countries = None
    if not start:
        start = None
    if not end:
        end = None
    chart = plot_reported_cases_per_million(countries,
                                            start,
                                            end)
    return chart.to_dict()


def main():
    """
    Main Function to start the web server

    """
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
