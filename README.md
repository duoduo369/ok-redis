# ok

Object-Key Mapper for Redis

If you've used redis on python, you've had to deal with redis keys. Sometimes,
_lots_ of redis keys. With so many keys, it's easy to make mistakes, especially
since keys are just strings. I built `ok` so that I didn't have to work with
strings for redis keys.

Here's how you use it:

```python
import ok
import redis


class User(ok.Key):
    fields = ['timeline', 'followers', 'following']


# Get user mixxorz' timeline
r = redis.StrictRedis()
r.zrevrange(User('mixxorz').timeline, 0, 50)
# ZREVRANGE User:mixxorz:timeline 0 50
```

Managing your keys just became a lot less fragile.

## Installation

Install it from pypi

```
$ pip install ok-redis
```

## Usage

Access fields.

```python
class User(ok.Key):
    fields = ['timeline', 'followers', 'following']


print(User('mixxorz').timeline)
# User:mixxorz:timeline
```

Chain keys.

```python
class City(ok.Key):
    fields = ['tweets_hll']


class Country(ok.Key):
    subkeys = [City]


print(Country('PH').City('Manila').tweets_hll)
# Country:PH:City:Manila:tweets
```

Access the class key

```python
class User(ok.Key):
    pass


print(User('mixxorz').key)
# User:mixxorz
```

IDs are optional.

```python
class User(ok.Key):
    fields = ['rankings']


print(User().rankings)
# User:rankings
```

You can change the string used for the key.

```python
class Facebook(ok.Key):
    fields = ['all_posts']
    class_key = 'fb'


print(Facebook().all_posts)
# fb:all_posts
```

## License

MIT
