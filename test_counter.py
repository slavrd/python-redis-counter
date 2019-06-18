import counter
import unittest
import os

class TestCounter(unittest.TestCase):
    """Tests the Counter class methods.
    Requires a redis running on localhost:6379 
    """

    # Initiate a Counter instance with connection to a local redis
    c = counter.Counter('localhost',6379,0,'count',os.getenv("REDIS_PASS"))

    def test_redis_connection(self):
        """Tests if c can connect to the redis
        """

        resp = self.c.r.execute_command('ping')
        self.assertEqual(resp, b'PONG')

    def test_get(self):
        """Tests Counter.get()
        """

        # Test if method returns 0 if value does not exist
        self.c.r.delete('count')
        self.assertEqual(0, self.c.get(), "get() did not return 0 on none existing key")

        # Test if method returns the value set in redis
        self.c.r.set('count', 5)
        self.assertEqual(5, self.c.get(), "get() did not return the correct value")

    def test_incr(self):
        """Tests Counter.incr()
        """

        # clear the redis key
        self.c.r.delete('count')

        # test that non-existent key is initialized
        self.c.incr()
        self.assertEqual(b'1', self.c.r.get('count'), "incr() did not initialized the correct value")

        # test that the values is increased by amount
        amount = 5
        ival = int(self.c.r.get('count'))
        self.c.incr(amount)
        cval = int(self.c.r.get('count'))
        self.assertEqual(amount, cval - ival, "incr() did not initialized the correct value")

if __name__ == "__main__":
    unittest.main()
