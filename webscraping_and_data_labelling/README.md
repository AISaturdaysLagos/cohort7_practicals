# Introduction to Web Scraping and Data Labelling
## Webscraping
- Install the required dependencies
```
cd webscraping_and_data_labelling
pip install -r requirements.txt
```
- Go through `scraper.ipynb` 
- Use your learnings from `scraper.ipynb` to complete the `scraper.py` 😃
## Access to live presentation slide
- Data Labelling with Label Studio: [Link to Slide](https://docs.google.com/presentation/d/1nZdH_ap8ykmRsz57pS87mqM4lcRIb9ilvkQQf4qYvXc/edit?usp=sharing)

## Conclusion
- By the end of this, you should have an understanding of how datasets are curated and labelled for machine learning projects. Some of the most popular datasets created by webscraping include
the [Pushshift Reddit Dump](https://files.pushshift.io/reddit/) and the [AfriFashion  Dataset](https://openaccess.thecvf.com/content/CVPR2021W/CVFAD/papers/Oyewusi_AFRIFASHION1600_A_Contemporary_African_Fashion_Dataset_for_Computer_Vision_CVPRW_2021_paper.pdf) 
- Yes, dataset creation is a valid research area and contribution!

## Other Tools & Projects
| S/N | Tool | Awesome projects |
| --- | ---- | ---------------- |
| 1 | [Scrapy](https://scrapy.org/) | [Nairaland](https://github.com/Olamyy/nairaland) |
| 2 | [Selenium](https://selenium-python.readthedocs.io/) | [AI4D-Dataset-Challenge](https://github.com/theyorubayesian/AI4D-Dataset-Challenge) |
| 3 | [Tweepy](https://docs.tweepy.org/en/stable/) | #TODO |

## Project Ideas
- Scrape a property listing website such as [Nigeria Property Centre](https://nigeriapropertycentre.com/) and create dataset for a Housing Price Regression problem
- Train a spacy-ner model on the corpus (find [here](https://github.com/masakhane-io/masakhane-ner/tree/main/data/pcm)), [this](https://towardsdatascience.com/train-ner-with-custom-training-data-using-spacy-525ce748fab7) tutorial can be of help. Then use the trained model to make prediction on the pidgin corpus that you scraped. You can then use label-studio to verify the predicted entities as done in [this](https://labelstud.io/blog/Evaluating-Named-Entity-Recognition-parsers-with-spaCy-and-Label-Studio.html) tutorial. 
