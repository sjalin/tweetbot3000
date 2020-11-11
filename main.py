import tweepy
import cred


class TwitterApi():
    api: tweepy.API = None

    def __init__(self):
        # Authenticate to Twitterpp
        auth = tweepy.OAuthHandler(cred.consumer_api_key, cred.consumer_api_key_secret)
        auth.set_access_token(cred.access_token, cred.access_token_secret)

        self.api = tweepy.API(auth)

        try:
            self.api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")


def main():
    print('Bot start, wosh!')
    t_api = TwitterApi()

    for tweet in t_api.api.search(q="trump ", lang="en", rpp=10, result_type='popular'):
        print(f"{tweet.user.name}:{tweet.text}")

#    t_api.api.update_status("Test")


if __name__ == '__main__':
    main()
