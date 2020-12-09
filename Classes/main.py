import tensorflow as tf
from grover.lm.modeling import sample
import random
from Classes.MakeStory import MakeStory
from Classes.globals import *


import random
import string

def get_random_string(length):
    letters = (' ' + string.ascii_lowercase)
    print((letters))
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
# get_random_string(8)
# get_random_string(8)
# get_random_string(6)


def send_story():
    print('starting making a story-------------------------------------------')
    ms = MakeStory()
    articles = []

    # Get the read headlines to look more realistic
    for feed_url in RSS_FEEDS_OF_REAL_STORIES_TO_EMULATE:
        articles += ms.get_articles_from_real_blog(feed_url)

    # Toss in the slanderous articles
    articles += ms.get_fake_articles()

    # Randomize the order the articles are generated
    random.shuffle(articles)



    encoder, news_config, tf_config = ms.load_model()

    final_title = []
    final_article = []
    with tf.Session(config=tf_config, graph=tf.Graph()) as sess:
        # Create the placehodler TensorFlow input variables needed to feed data to Grover model
        # to make new predictions.
        initial_context = tf.placeholder(tf.int32, [1, None])
        p_for_topp = tf.placeholder(tf.float32, [1])
        eos_token = tf.placeholder(tf.int32, [])
        ignore_ids = tf.placeholder(tf.bool, [news_config.vocab_size])

        # Load the model config to get it set up to match the pre-trained model weights
        tokens, probs = sample(
            news_config=news_config,
            initial_context=initial_context,
            eos_token=eos_token,
            ignore_ids=ignore_ids,
            p_for_topp=p_for_topp,
            do_topk=False
        )

        # Restore the pre-trained Grover 'huge' model weights
        saver = tf.train.Saver()
        saver.restore(sess, MODEL_CKPT)

        # START MAKING SOME FAKE NEWS!!
        # Loop through each headline we scraped from an RSS feed or made up
        for article in articles:
            print(f"Building article from headline '{article['title']}'")

            # If the headline is one we made up about a specific person, it needs special handling
            if NAME_TO_SLANDER in article['title']:
                # The first generated article may go off on a tangent and not include the target name.
                # In that case, re-generate the article until it at least talks about our target person
                attempts = 0
                while NAME_TO_SLANDER not in article['text']:
                    print(attempts)
                    # Generate article body given the context of the real blog title
                    article['text'] = ms.generate_article_attribute(sess, encoder, tokens, probs, article,initial_context,eos_token,ignore_ids,p_for_topp, target="article")

                    # If the Grover model never manages to generate a good article about the target victim,
                    # give up after 10 tries so we don't get stuck in an infinite loop
                    attempts += 1
                    if attempts > 50:
                        continue
            # If the headline was scraped from an RSS feed, we can just blindly generate an article
            else:
                article['text'] = ms.generate_article_attribute(sess, encoder, tokens, probs, article,initial_context,eos_token,ignore_ids,p_for_topp, target="article")

            # Now, generate a fake headline that better fits the generated article body
            # This replaces the real headline so none of the original article content remains
            article['title'] = ms.generate_article_attribute(sess, encoder, tokens, probs, article,initial_context,eos_token,ignore_ids,p_for_topp, target="title")

            # Grab generated text results so we can post them to WordPress
            article_title = article['title']
            article_text = article['text']
            article_date = article["iso_date"]
            article_image_url = article["image_url"]
            article_tags = article['tags']

            print(f" - Generated fake article titled '{article_title}'")
            print(NAME_TO_SLANDER)
            print((article_title),'--------------')
            print((article_text),'--------------')
            print((article_date),'--------------')

            return article_title, article_text

def send_story1():
    article_title = get_random_string(8)
    article_text = get_random_string(1000)
    return article_title,article_text