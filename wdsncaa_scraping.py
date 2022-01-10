#!/usr/bin/env python
# coding: utf-8

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager

def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    
    # Execute scrape func and store results in dictionary
    data = {
          "wds_last_modified": dt.datetime.now(),
          "wds_ncaafb": sports_news(browser)
    }

    # Stop webdriver and return data
    browser.quit()
    return data


def sports_news(browser):

    # Visit the mars nasa news site
    #url = 'https://www.espn.com/college-football/game/_/gameId/401331229'
    url = 'https://www.espn.com/college-football/game/_/gameId/401331242'
    browser.visit(url)


    # Scrape Away Team Data
    html = browser.html
    awayteam_soup = soup(html, 'html.parser')
    awayteam_tag = awayteam_soup.find("div", class_="team away")  #id="custom-nav")

    # Get Away Team Name
    getawayteamspan = awayteam_tag.find_all("span")
    for team in getawayteamspan:
            awayteam = team.text
    print(f"Away Team Name: {awayteam}")

    # Get Away Team Logo
    html = browser.html
    getawayteamlogo_soup = soup(html, 'html.parser')
    awayteam_tag = getawayteamlogo_soup.find("div", class_="team away") 
    getawaylogo = awayteam_tag.find("div", class_="team-info-logo")  

    awayteamimg_href = getawaylogo.find("a")
    scr_awayteamimg_href = awayteamimg_href.find("img").get("src")
    awayteamlogo_img = scr_awayteamimg_href
    print (f"{awayteam} Team Logo : {awayteamlogo_img}")

    # Get Away Team Score
    html = browser.html
    getawayteamscore_soup = soup(html, 'html.parser')
    getawayteamscoretag = getawayteamscore_soup.find("div", class_="score icon-font-after")
    awayteam_score = getawayteamscoretag.text
    print(f"{awayteam} Score: {awayteam_score}")

    # Scape Home Team data

    html = browser.html
    ncaa_soup = soup(html, 'html.parser')
    hometeamtag = ncaa_soup.find("div", class_="team home")

    # Get Home Team Name
    hometeamspan = hometeamtag.find_all("span")
    for team in hometeamspan:
            hometeam = team.text
    print(f"Home Team Name: {hometeam}")

    # Get Home Team Logo
    html = browser.html
    gethometeamlogo_soup = soup(html, 'html.parser')
    gethometeam = gethometeamlogo_soup.find("div", class_="team home")
    gethometeamlogo = gethometeam.find("div", class_="team-info-logo")

    hometeamimg_href = gethometeamlogo.find("a")
    scr_hometeamimg_href = hometeamimg_href.find("img").get("src")
    hometeamlogo_img = scr_hometeamimg_href
    print (f"{hometeam} Team Logo : {hometeamlogo_img}")

    # Get Home Team Score
    html = browser.html
    gethometeamscore_soup = soup(html, 'html.parser')
    gethometeamtag = gethometeamlogo_soup.find("div", class_="team home")
    gethometeamscoretag = gethometeamtag.find("div", class_="score icon-font-before")
    hometeam_score = gethometeamscoretag.text
    print(f"{hometeam} Score: {hometeam_score}")

    game_time = {}
    game_time = {"gametype" : "Championship", 
                 "awayteam" : awayteam, 
                 "awayteam_logo_img" : awayteamlogo_img,
                 "awayteam_score" : awayteam_score, 
                 "hometeam" : hometeam, 
                 "hometeam_logo_img" : hometeamlogo_img, 
                 "hometeam_score" : hometeam_score
                }

    game_time
    return game_time


if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())


