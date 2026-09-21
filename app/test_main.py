from unittest.mock import MagicMock, patch
from app.main import can_access_google_page

@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_accessible(
    mock_valid_google_url: MagicMock, mock_has_internet_connection: MagicMock, url: str
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = True
    result = can_access_google_page(url)
    assert result == "Accessible"



@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_no_internet(
    mock_has_internet_connection: MagicMock, mock_valid_google_url: MagicMock, url: str
) -> None:
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = True
    result = can_access_google_page(url)
    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_invalid_url(
    mock_has_internet_connection: MagicMock, mock_valid_google_url: MagicMock, url: str
) -> None:
    mock_has_internet_connection.return_value = True
    mock_valid_google_url.return_value = False
    result = can_access_google_page(url)
    assert result == "Not accessible"


@patch("app.main.has_internet_connection")
@patch("app.main.valid_google_url")
def test_can_access_google_page_invalid_url_and_no_internet(
    mock_has_internet_connection: MagicMock, mock_valid_google_url: MagicMock, url: str
) -> None:
    mock_has_internet_connection.return_value = False
    mock_valid_google_url.return_value = False
    result = can_access_google_page(url)
    assert result == "Not accessible"
