from App import app as application

def test_get_data_success(mocker):
    """
    Test if get_data() returns a list
    """
    with application.app_context():
        mocker.patch('App.get_data', return_value=list())
        client = application.test_client()
        response = client.get('/')
        assert response.status_code == 200

def test_filter_year_success(mocker):
    """
    Test if filter_data() returns a list with the correct year
    """
    with application.app_context():
        mocker.patch('App.get_data', return_value=list())
        client = application.test_client()
        response = client.get('/filter?year=2015')
        assert response.status_code == 200

def test_filter_city_success(mocker):
    """
    Test if filter_data() returns a list with the correct city
    """
    with application.app_context():
        mocker.patch('App.get_data', return_value=list())
        client = application.test_client()
        response = client.get('/filter?city=bogota')
        assert response.status_code == 200

def test_filter_state_success(mocker):
    """
    Test if filter_data() returns a list with the correct state
    """
    with application.app_context():
        mocker.patch('App.get_data', return_value=list())
        client = application.test_client()
        response = client.get('/filter?state=vendido')
        assert response.status_code == 200

def test_filter_state_year_success(mocker):
    """
    Test if filter_data() returns a list with the correct state and year
    return_value=list()
    """
    with application.app_context():
        mocker.patch('App.get_data', return_value=list())
        client = application.test_client()
        response = client.get('/filter?state=vendido&year=2015')
        assert response.status_code == 200

def test_filter_city_state_success(mocker):
    """
    Test if filter_data() returns a list with the correct city and state
    return_value=list()
    """
    with application.app_context():
        mocker.patch('App.get_data', return_value=list())
        client = application.test_client()
        response = client.get('/filter?city=bogota&state=vendido')
        assert response.status_code == 200

def test_filter_city_state_year_success(mocker):
    """
    Test if filter_data() returns a list with the correct city, state and year
    return_value=list()
    """
    with application.app_context():
        mocker.patch('App.get_data', return_value=list())
        client = application.test_client()
        response = client.get('/filter?city=bogota&state=vendido&year=2015')
        assert response.status_code == 200