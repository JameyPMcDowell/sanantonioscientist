from flask import url_for

from lib.tests import assert_status_with_message


class TestContact:
    def test_contact_page(self, client):
        """Contact page should respond with a success 200."""
        response = client.get(url_for('contact.index'))
        assert response.status_code == 200

    def contact_form(self, client):
        """Contact form should redirect with a message."""
        form = {
            'email': 'foo@bar.com',
            'message': 'Test message for San Antonio Scientist.'
        }

        response = client.post(
            url_for('contact.index'),
            data=form,
            follow_redirects=True
        )
        assert_status_with_message(200, response, 'Thanks')
