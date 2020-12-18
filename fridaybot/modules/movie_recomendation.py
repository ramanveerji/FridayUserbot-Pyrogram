from bs4 import BeautifulSoup as SOUP 
import re 
import requests as HTTP 
from uniborg.util import friday_on_cmd
from fridaybot import CMD_HELP
from fridaybot.utils import admin_cmd




@friday.on(admin_cmd(pattern="movie (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    def main(emotion): 
      if(emotion == "Sad"): 
        urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'


      elif(emotion == "Anticipation"): 
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'
 
      elif(emotion == "Fear"): 
        urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'


      elif(emotion == "Enjoyment"): 
        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

      elif(emotion == "Trust"): 
        urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'
       
      
      
      response = HTTP.get(urlhere) 

      data = response.text 
      soup = SOUP(data, "lxml") 
      title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
      return title 


    emotion = input_str
    a = main(emotion) 
    count = 0
    sed = ''
    if(emotion == "Disgust" or emotion == "Anger" or emotion=="Surprise"): 
      for i in a: 
        tmp = str(i).split('>;') 
        if(len(tmp) == 3): 
          lol = tmp[1][:-3]
          sed += lol + "\n"
          if(count > 13): 
            break
          count += 1

    else: 
      for i in a: 
        tmp = str(i).split('>') 
        if(len(tmp) == 3): 
          lol = tmp[1][:-3]
          sed += lol + "\n"
        if(count > 11): 
          break
        count+=1
    await event.edit(
      f"<b><u>Below Are Your Movie Recommendations</b></u>\n\n<b>Your Emotion:- <code>{input_str}</code>\n<b>Recommended Movie List:- </b><code>{sed}</code>", parse_mode="HTML",)
  