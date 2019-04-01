from utils import get_short_url


class DuplicateError(Exception):
    def __init__(self, message):
        self.message = message


db_url = {}


def add_to_db(original_url):
    short_url = get_short_url()
    if get_from_db(short_url) != None:
        raise DuplicateError('Duplicate url find in database =)')
    else:
        db_url.update(dict(short_url=short_url, original_url=original_url))
        return short_url


def get_from_db(short_url):
    for short_url in db_url.items():
        if short_url == short_url:
            return db_url.get('original_url')


def main():
    short_url = add_to_db('www.gooogle.com/dfjvsviosmsvprlglgp/rgoeuhjowivpow.jpg')
    print(db_url)
    print(get_from_db(short_url))


if __name__ == "__main__":
    main()
