import inspect

try:
    from unittest import mock
except ImportError:
    import mock
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.common.exceptions import NoSuchElementException


from page_objects import PageObject, PageElement, MultiPageElement


@pytest.fixture()
def webdriver():
    return mock.Mock(spec=WebDriver)


class TestConstructor:

    def test_page_element(self):
        elem = PageElement(css='foo')
        assert elem.locator == (By.CSS_SELECTOR, 'foo')

    def test_multi_page_element(self):
        elem = MultiPageElement(id_='bar')
        assert elem.locator == (By.ID, 'bar')

    def test_page_element_bad_args(self):
        with pytest.raises(ValueError):
            PageElement()
        with pytest.raises(ValueError):
            PageElement(id_='foo', xpath='bar')


class TestGet:
    def test_get_descriptors(self, webdriver):
        class TestPage(PageObject):
            test_elem1 = PageElement(css='foo')
            test_elem2 = PageElement(id_='bar')

        webdriver.find_element.side_effect = ["XXX", "YYY"]
        page = TestPage(webdriver=webdriver)
        assert page.test_elem1 == "XXX"
        assert page.test_elem2 == "YYY"
        assert webdriver.find_element.mock_calls == [
            mock.call(By.CSS_SELECTOR, 'foo'),
            mock.call(By.ID, 'bar'),
        ]

    def test_get_element_with_context(self, webdriver):
        class TestPage(PageObject):
            test_elem = PageElement(css='bar', context=True)

        page = TestPage(webdriver=webdriver)
        elem = mock.Mock(spec=WebElement, name="My Elem")
        res = page.test_elem(elem)
        assert elem.find_element.called_once_with(By.CSS_SELECTOR, 'bar')
        assert res == elem.find_element.return_value

    def test_get_not_found(self, webdriver):
        class TestPage(PageObject):
            test_elem = PageElement(css='bar')

        page = TestPage(webdriver=webdriver)
        webdriver.find_element.side_effect = NoSuchElementException
        assert page.test_elem is None

    def test_get_unattached(self):
        assert PageElement(css='bar').__get__(None, None) is None

    def test_get_multi(self, webdriver):
        class TestPage(PageObject):
            test_elems = MultiPageElement(css='foo')

        webdriver.find_elements.return_value = ["XXX", "YYY"]
        page = TestPage(webdriver=webdriver)
        assert page.test_elems == ["XXX", "YYY"]
        assert webdriver.find_elements.called_once_with(By.CSS_SELECTOR, 'foo')

    def test_get_multi_not_found(self, webdriver):
        class TestPage(PageObject):
            test_elems = MultiPageElement(css='foo')

        webdriver.find_elements.side_effect = NoSuchElementException
        page = TestPage(webdriver=webdriver)
        assert page.test_elems == []


class TestSet:
    def test_set_descriptors(self, webdriver):
        class TestPage(PageObject):
            test_elem1 = PageElement(css='foo')

        page = TestPage(webdriver=webdriver)
        elem = mock.Mock(spec=WebElement, name="My Elem")
        webdriver.find_element.return_value = elem
        page.test_elem1 = "XXX"
        assert webdriver.find_elements.called_once_with(By.CSS_SELECTOR, 'foo')
        elem.send_keys.assert_called_once_with('XXX')

    def test_cannot_set_with_context(self, webdriver):
        class TestPage(PageObject):
            test_elem = PageElement(css='foo', context=True)

        page = TestPage(webdriver=webdriver)
        with pytest.raises(ValueError) as e:
            page.test_elem = 'xxx'
        assert "doesn't support elements with context" in e.value.args[0]

    def test_cannot_set_not_found(self, webdriver):
        class TestPage(PageObject):
            test_elem = PageElement(css='foo')

        page = TestPage(webdriver=webdriver)
        webdriver.find_element.side_effect = NoSuchElementException

        with pytest.raises(ValueError) as e:
            page.test_elem = 'xxx'
        assert "element not found" in e.value.args[0]

    def test_set_multi(self, webdriver):
        class TestPage(PageObject):
            test_elems = MultiPageElement(css='foo')

        page = TestPage(webdriver=webdriver)
        elem1 = mock.Mock(spec=WebElement)
        elem2 = mock.Mock(spec=WebElement)
        webdriver.find_elements.return_value = [elem1, elem2]
        page.test_elems = "XXX"
        assert webdriver.find_elements.called_once_with(By.CSS_SELECTOR, 'foo')
        elem1.send_keys.assert_called_once_with('XXX')
        elem2.send_keys.assert_called_once_with('XXX')

    def test_cannot_set_multi_with_context(self, webdriver):
        class TestPage(PageObject):
            test_elem = MultiPageElement(css='foo', context=True)

        page = TestPage(webdriver=webdriver)
        with pytest.raises(ValueError) as e:
            page.test_elem = 'xxx'
        assert "doesn't support elements with context" in e.value.args[0]

    def test_cannot_set_multi_not_found(self, webdriver):
        class TestPage(PageObject):
            test_elem = MultiPageElement(css='foo')

        page = TestPage(webdriver=webdriver)
        webdriver.find_elements.side_effect = NoSuchElementException

        with pytest.raises(ValueError) as e:
            page.test_elem = 'xxx'
        assert "no elements found" in e.value.args[0]


class TestRootURI:

    class TestPage(PageObject):
        pass

    def test_from_constructor(self, webdriver):
        page = self.TestPage(webdriver=webdriver, root_uri="http://example.com")
        assert page.root_uri == 'http://example.com'

    def test_from_webdriver(self):
        webdriver = mock.Mock(spec=WebDriver, root_uri="http://example.com/foo")
        page = self.TestPage(webdriver=webdriver)
        assert page.root_uri == 'http://example.com/foo'

    def test_get(self, webdriver):
        page = self.TestPage(webdriver=webdriver, root_uri="http://example.com")
        page.get('/foo/bar')
        assert webdriver.get.called_once_with("http://example.com/foo/bar")

    def test_get_no_root(self, webdriver):
        page = self.TestPage(webdriver=webdriver)
        page.get('/foo/bar')
        assert webdriver.get.called_once_with("/foo/bar")
