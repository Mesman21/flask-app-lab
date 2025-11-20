import unittest
from app import create_app, db
from app.posts.models import Post


class PostsTestCase(unittest.TestCase):

    def setUp(self):

        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()


        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):

        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_post(self):
        """Тест створення нового поста"""

        response = self.client.post('/post/create', data={
            'title': 'Test Post',
            'content': 'This is a test content',
            'category': 'news',
            'is_active': 'y'  # 'y' або 'on' для чекбокса
        }, follow_redirects=True)


        post = Post.query.filter_by(title='Test Post').first()
        self.assertIsNotNone(post)
        self.assertEqual(post.content, 'This is a test content')


        self.assertIn(b'Post created successfully', response.data)

    def test_list_posts(self):
        """Тест відображення списку постів"""

        p = Post(title="List Test", content="Content", category="tech")
        db.session.add(p)
        db.session.commit()


        response = self.client.get('/post')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'List Test', response.data)

    def test_delete_post(self):
        """Тест видалення поста"""
        p = Post(title="To Delete", content="Delete me", category="other")
        db.session.add(p)
        db.session.commit()


        response = self.client.post(f'/post/{p.id}/delete', follow_redirects=True)


        post = Post.query.filter_by(title='To Delete').first()
        self.assertIsNone(post)
        self.assertIn(b'Post has been deleted', response.data)


if __name__ == '__main__':
    unittest.main()