# Wrapped-Eggler
Spotify Music Analysis using the Spotify API

Ideas:

# - Data Visualization (charts, graphs)
# - Top Genres Analysis DONE
# - Audio Features Analysis
# - Playlist Creation based off of listening habits
# - Shareable Results
# - Add more API calls to the dashboard view (e.g., top artists, recently played).
# - Create a new view and template to handle D3.js visualizations. The view would
#   return a JSON response of the data, and the template would use JavaScript
#   to fetch this JSON and render the charts.
# - Implement Django models to store the data permanently in your database,
#   so you don't have to re-fetch it from Spotify every time.
# - Improve the styling of your dashboard and visualizations.
# - Find a way to say how many times you have listened to your top tracks
# - implement a recently played section
# - Also get the ReadMe to be a proper description of the file and what i did


Genre Charts needs to be cleaned up and documented
All .html and .js need to be cleaned up and documented
Views.py needs to be cleaned up and documented
Inspired by stats for spotify make it show 3 different time periods for top tracks (4 weeks, 6 months, 12 months) and you can select which you'd like to see. Do the same thing for artists and tracks and genres but use bar graphs for that. 
A recently played tracks thing would be cool as well and probably quite easy
MAKE IT LOOK VISUALLY APPEALING TO THE USER SO PRETTY MUCH HOW I WOULD LIKE TO LOOK AT IT.

8/7/25:
Got top tracks page working how I want it to work. Songs numbered and showing 50 top tracks now. Working time frames as well. I think it could be cool if you could make a playlist from these set of 50 songs as well.
Rewrote the top tracks view and now need to change the html to list the top 50 but also be able to switch between the time frames.

Got top tracks done. Need to figure something else out for the genre view. I think a pie chart that shows what percentage of the last time frame you listened to each genre.

Genre analysis is weird I am not too sure what I want it to do. Might just scrap it for now and focus on getting the html to look cleaner.
Cleaned up the dashboard html. Still want to change the overall look of it in general but thats a later problem. 
Now onto working on a new and better genre analysis.
Change it from all time ot 12 months i think (look into this)

Okay got something cool for genres but the logic is just messed up. Dont need it to actually try to estimate the amount of minutes. Change this later.