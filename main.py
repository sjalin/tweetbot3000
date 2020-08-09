import tweepy
import cred


class TwitterApi():
    api: tweepy.API = None

    def __init__(self):
        # Authenticate to Twitterpp
        auth = tweepy.OAuthHandler(cred.consumer_api_key, cred.consumer_api_key_secret)
        auth.set_access_token(cred.access_token, cred.access_token_secret)

        self.api = tweepy.api(auth)


def main():
    t_api = TwitterApi()
    t_api.api.update_status("Testpip")


if __name__ == '___main___':
    main()
