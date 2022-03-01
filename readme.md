### SENTIMENT ANALYSIS ON DJANGO APP

- I warn you, all steps of the project is for adding emojis like 🙂 and 😤 to  movie comments (as sentiments).

I made this project in a day (as weekend project) to warm up with Django more and use a Bert Model / Transformers on it. 

Used concepts in the projects:
- Django web app,
- Flask Resp API
- Web Scraping
- Sentiment Analysis (with pretrained model)

-----

- I took the dataset from kaggle and used pretrained bert model on it. And checked if this pretrained model works well or not. (it is good enough) You can find it [here](NOTEBOOKS/part1_nlp_bert.ipynb).
- After this I needed header photos of the movies in tha dataset. (They are not included in the dataset.) So I made a little web scraping part in my project to take images. Actually I didnt take images, I only took their image urls. [here](NOTEBOOKS/part2_scrape_images.ipynb)
- And I put the preprocessing part of the sentiment analysis and pretrained bert transformers model in Flask Rest API. [here](REST)
- And lastly I made a simple Django app to show intermediate steps and the interface. [here](https://github.com/bilative/sentiment-analysis-on-DJANGO/tree/main/DJANGO_APP/MovieApp)

-----
How I planned this project before I started.
![plan](https://user-images.githubusercontent.com/70684994/156235126-0549c076-65cf-4681-80af-5e7bf2859850.png)


Sample screenshots from the app:

![mumya1](https://user-images.githubusercontent.com/70684994/155902854-b2c024ed-d53f-4499-bab3-f8b780401e47.png)
![mumya2](https://user-images.githubusercontent.com/70684994/155902855-c13d7cd8-ba76-4bfe-8790-aae7fd4b3fb9.png)
![mumya3](https://user-images.githubusercontent.com/70684994/155902856-46706155-7633-48c2-8eb9-9af11c105ba0.png)
![image4](https://user-images.githubusercontent.com/70684994/155972807-3e367e3d-c145-4e99-9f72-3fedff897a2c.png)
![Mucize](https://user-images.githubusercontent.com/70684994/155902857-6f7308db-7083-48ec-bc68-0b0ed3c4e486.png)

------
Dynamic url logic is little wrong in the project. Turkish characters in the url like /movies/türkçe-özel/ is not supported by Django. I realized it in the end but didnt fixed.
I didnt dockerized the app, because bert model required anaconda, I didnt try it to save time.
