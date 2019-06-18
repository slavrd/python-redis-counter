import redis
import os

class Counter:
    """Represents a counter that stores it's value in a Redis db
    """

    def __init__(self, rhost: str, rport: int, rdb: int, rkey: str, rpass :str=None):
        """A constructor for Counter using the provided connection details
        """
        self.r = redis.Redis(host=rhost, port=rport, db=rdb, password=rpass)
        self.rkey = rkey

    def incr(self, amount=1):
        """Increases the value of the counter with amount.
        If self.rkey does not exist in redis initializes it with amount
        """
        
        self.r.incr(self.rkey, amount)

    def get(self) -> int:
        """Get the current value of the counter
        """

        val = self.r.get(self.rkey)
        if val == None:
            return 0
        else:
            return int(val)

if __name__ == '__main__':
    c = Counter(os.getenv('REDIS_ADDR'),6379,0,'count',os.getenv('REDIS_PASS'))
    c.incr()
    print(c.get())
