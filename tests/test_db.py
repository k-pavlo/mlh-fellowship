import unittest
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]

# use an in-memory SQLite for tests.
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp( self):
        # Bind model classes to test db. Since we have a complete list of
        # all models, we do not need to recursively bind dependencies.
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables (MODELS)

    def tearDown (self):
        # Not strictly necessary since SQLite in-memory databases only live
        # for the duration of the connection, and in the next step we close
        # the connection...but a good practice all the same.
        test_db.drop_tables (MODELS)

        # Close connection to db.
        test_db.close( )

    def test_timeline_post(self) :
        # Create 2 timeline posts.
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')
        assert second_post.id == 2

    # get timeline posts and assert that they are correct
    def test_timeline_get(self):
        # check the initial state of the database
        posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())
        assert posts.count() == 0

        # check if the post was created correctly
        TimelinePost.create(name='John', email='john@example.com', content='Hi from John!')
        posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())
        assert posts.count() == 1
        assert posts[0].id == 1
        assert posts[0].name == 'John'

        # create 2 posts and check if they are in descending order
        TimelinePost.create(name='Jane', email='jane@example.com', content='Hi from Jane!')
        posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())
        assert posts.count() == 2
        assert posts[0].id == 2
        assert posts[0].name == 'Jane'
        assert posts[1].id == 1
        assert posts[1].name == 'John'
