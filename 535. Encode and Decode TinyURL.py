import random
import string


class Codec:
    def __init__(self):
        self.url_map = {}
        self.base_url = "http://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        key = "".join(
            random.choice(string.ascii_letters + string.digits) for _ in range(6)
        )
        while key in self.url_map:
            key = "".join(
                random.choice(string.ascii_letters + string.digits) for _ in range(6)
            )
        self.url_map[key] = longUrl
        return self.base_url + key

    def decode(self, shortUrl: str) -> str:
        key = shortUrl.split("/")[-1]
        return self.url_map.get(key, "")


codec = Codec()
short = codec.encode("https://www.yawar.com")
print("Short URL:", short)
print("Original URL:", codec.decode(short))
