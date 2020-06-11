
tweets = [
    {
        "id": 100200297,
        "full_text": "Look at this delicious sandwich!",
        "img_url": "https://sandwhoa.com/sandwich.png",
        "user": {"screen_name": "sandwhoa", "followers": 5000},
        "likes_count": 150
    },
    {
        "id": 100200298,
        "full_text": "I love sandwiches",
        "img_url": None,
        "user": {"screen_name": "person1", "followers": 100},
        "likes_count": 5
    },
    {
        "id": 100200299,
        "full_text": "@sandwhoa yumm...",
        "img_url": None,
        "user": {"screen_name": "person2", "followers": 200},
        "likes_count": 10
    },
    {
        "id": 100200300,
        "full_text": "@sandwhoa that sandwich looks amazing!!",
        "img_url": None,
        "user": {"screen_name": "person3", "followers": 300},
        "likes_count": 35
    },
    {
        "id": 100200301,
        "full_text": "I ate a great sandwich today",
        "img_url": None,
        "user": {"screen_name": "person4", "followers": 400},
        "likes_count": 50
    }
]

if __name__ == "__main__":

    print("------------------")
    print("PROCESSING SOCIAL MEDIA DATA...")
    print("------------------")
    #print(tweets)

    # breakpoint()

    #
    # QUESTION A
    #
    # "Print" the screen name of the user who authored the first tweet (i.e. "sandwhoa"):
    print(tweets[0]["user"]["screen_name"])


    #
    # QUESTION B
    #
    # Of all the tweets which include the phrase "@sandwhoa" in their full text,
    # ... "print" the screen name of the user who authored that tweet,
    # ... each on a separate line (i.e. "person2", then "person3"):

    def contains_shop(message):
        return "@sandwhoa" in message["full_text"]

    at_us = list(filter(contains_shop, tweets))

    users = ([n["user"]["screen_name"] for n in at_us])
    print(*users,sep='\n')


    

    #
    # QUESTION C
    #
    # Of all the tweets which include the phrase "@sandwhoa" in their full text,
    # ... determine which tweet has the greatest number of likes,
    # ... and then "print" the screen name of the user who authored that tweet (i.e. "person3").
    # ... FYI: Assume the tweet order can change at any time
    # ... and has no relationship with the number of likes.

    def top_tweet(all_tweets):
         return max(all_tweets, key=lambda best: best["likes_count"])
    
    
    influencer = (top_tweet(tweets))
    
    print(str(influencer["user"]["screen_name"]))