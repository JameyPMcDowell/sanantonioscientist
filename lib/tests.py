def assert_status_with_message(status_code=200, response=None, message=None):
    """Check to see if a message is contained within a response.

    Parameters
    ----------
    status_code : int, optional
        status code that defaults to 200, by default 200
    response : str, optional
        Flask response, by default None
    message : str, optional
        String to check for, by default None
    """
    assert response.status_code == status_code
    assert message in str(response.data)
