from unittest.mock import MagicMock, patch


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_accessible(
    mock_valid_google_url: MagicMock, mock_has_internet_connection: MagicMock
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_no_internet(
    mock_has_internet_connection: MagicMock, mock_valid_google_url: MagicMock
) -> None:
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = True


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_invalid_url(
    mock_has_internet_connection: MagicMock, mock_valid_google_url: MagicMock
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_invalid_url_and_no_internet(
    mock_has_internet_connection: MagicMock, mock_valid_google_url: MagicMock
) -> None:
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = False
