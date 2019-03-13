from ad_classes import AdClasses
from ad_renderer import AdRenderer
from unittest.mock import patch

@patch('cv2.imshow')
@patch('cv2.imread')
def test_should_render_ad_for_class(im_read_mock, im_show_mock):
    im_read_mock.return_value = "bleh"

    AdRenderer().render(AdClasses.GENERIC)

    im_show_mock.assert_called_with("img", "bleh")
    im_read_mock.assert_called_with("images/soccer_ball.jpg")
