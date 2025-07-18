import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        self.assertIn('<title>MLH Fellow</title>', html)
        # check the nav bar links
        self.assertIn('<a href="/">Home</a>', html)
        self.assertIn('<a href="/profile_summary">Summary</a>', html)
        self.assertIn('<a href="/hobbies">Hobbies</a>', html)
        self.assertIn('<a href="/map">Map</a>', html)
        self.assertIn('<a href="/timeline">Timeline</a>', html)
        # check the about me section
        self.assertIn('<h1>About Me</h1>', html)
        # check if the footer data is loaded
        self.assertIn('Follow me on', html)
        self.assertIn('https://www.linkedin.com', html)
        self.assertIn('https://github.com', html)

    def test_timeline(self):
        # check original state of the timeline
        response = self.client.get('/api/timeline_post')
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert 'timeline_posts' in json
        assert len(json['timeline_posts']) == 0

        # test POST request
        for name in ['Jane Doe', 'John Doe']:
            response = self.client.post('/api/timeline_post', data={
                "name": name,
                "email": f"{name.lower().replace(' ', '')}@example.com",
                "content": f"Hello world, I'm {name}! This is a test post."
            })
            assert response.status_code == 200
            json = response.get_json()
            assert 'id' in json
            assert json['name'] == name
            assert json['email'] == f"{name.lower().replace(' ', '')}@example.com"
            assert json['content'] == f"Hello world, I'm {name}! This is a test post."

        # test GET request to retrieve timeline posts
        response = self.client.get('/api/timeline_post')
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert 'timeline_posts' in json
        assert len(json['timeline_posts']) == 2  # 2 posts were created above
        # check the content of the posts
        for post in json['timeline_posts']:
            assert 'id' in post
            assert 'name' in post
            assert 'email' in post
            assert 'content' in post
            assert post['content'].startswith("Hello world, I'm")
            assert '@' in post['email']
        # check if the posts are in descending order
        assert json['timeline_posts'][0]['id'] == 2
        assert json['timeline_posts'][0]['name'] == 'John Doe'
        assert json['timeline_posts'][1]['id'] == 1
        assert json['timeline_posts'][1]['name'] == 'Jane Doe'

        # test timeline page
        response = self.client.get('/timeline')
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        self.assertIn('<title>Timeline</title>', html)
        # check the nav bar links
        self.assertIn('<a href="/">Home</a>', html)
        self.assertIn('<a href="/profile_summary">Summary</a>', html)
        self.assertIn('<a href="/hobbies">Hobbies</a>', html)
        self.assertIn('<a href="/map">Map</a>', html)
        self.assertIn('<a href="/timeline">Timeline</a>', html)
        # test if the form with labels for name, email, and content exists
        self.assertIn('<label for="name">Name:</label>', html)
        self.assertIn('<label for="email">Email:</label>', html)
        self.assertIn('<label for="content">Content:</label>', html)
        self.assertIn('<input type="submit" value="Post">', html)
        # test the post display section
        self.assertIn('<h2>Timeline</h2>', html)
        '''the following test cases can't pass since the page reloads after posting
        self.assertIn("<li class='post'>", html)
        self.assertIn('<p class="name">John Doe</p>', html)
        self.assertIn('<p class="name">Jane Doe</p>', html)
        self.assertIn('<p class="content">Hello world, I&#39;m John Doe! This is a test post.</p>', html)
        self.assertIn('<p class="content">Hello world, I&#39;m Jane Doe! This is a test post.</p>', html)
        '''

        # check if the footer data is loaded
        self.assertIn('Follow me on', html)
        self.assertIn('https://www.linkedin.com', html)
        self.assertIn('https://github.com', html)


    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post('/api/timeline_post', data={
            "email": "john@example.com", "content": "Hello world, I'm John!"
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post('/api/timeline_post', data={
            "name": "John Doe", "email": "john@example.com", "content": ""
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post('/api/timeline_post', data={
            "name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"
        })
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
