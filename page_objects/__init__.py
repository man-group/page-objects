from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class PageObject(object):
    """Page Object pattern.

    :param webdriver: `selenium.webdriver.WebDriver`
        Selenium webdriver instance
    :param root_uri: `str`
        Root URI to base any calls to the ``PageObject.get`` method. If not defined
        in the constructor it will try and look it from the webdriver object.
    """
    def __init__(self, webdriver, root_uri=None):
        self.w = webdriver
        self.root_uri = root_uri if root_uri else getattr(self.w, 'root_uri', None)

    def get(self, uri):
        """
        :param uri:  URI to GET, based off of the root_uri attribute.
        """
        root_uri = self.root_uri or ''
        self.w.get(root_uri + uri)


class PageElement(object):
    """Page Element pattern.

     :param webdriver: `selenium.webdriver.WebDriver`
         Selenium webdriver instance

     Requires the ``locator`` attribute to be set as:
        (`selenium.webriver.common.by.By`, locator text)

     Eg: 'login.username': (By.ID, 'username'),  (By.XPATH, '//password)'

    """
    locator = None

    def __init__(self):
        assert self.locator is not None

    def __get__(self, instance, owner):
        if not instance:
            return None
        try:
            return instance.w.find_element(*self.locator)
        except NoSuchElementException:
            return None

    def __set__(self, instance, value):
        elem = self.__get__(instance, None)
        if not elem:
            raise ValueError("Can't set value, element not found")
        elem.send_keys(value)


class MultiPageElement(PageElement):
    """ Like `_PageElement` but returns multiple results
    """
    def __get__(self, instance, owner):
        try:
            return instance.w.find_elements(*self.locator)
        except NoSuchElementException:
            return []


# Map factory arguments to webdriver locator enums
_LOCATOR_MAP = {'css': By.CSS_SELECTOR,
                'id_': By.ID,
                'name': By.NAME,
                'xpath': By.XPATH,
                'link_text': By.LINK_TEXT,
                'partial_link_text': By.PARTIAL_LINK_TEXT,
                'tag_name': By.TAG_NAME,
                'class_name': By.CLASS_NAME,
                }


def page_element(klass=PageElement, **kwargs):
    """ Factory method for page elements

    :param css:    `str`
        Use this css locator
    :param id_:    `str`
        Use this element ID locator
    :param name:    `str`
        Use this element name locator
    :param xpath:    `str`
        Use this xpath locator
    :param link_text:    `str`
        Use this link text locator
    :param partial_link_text:    `str`
        Use this partial link text locator
    :param tag_name:    `str`
        Use this tag name locator
    :param class_name:    `str`
        Use this class locator

    Page Elements can be used like this::

        >>> from page_objects import PageObject, page_element
        >>> class MyPage(PageObject):
                elem1 = page_element(css='div.myclass')
                elem2 = page_element(id_='foo')

    """
    if not kwargs:
        raise ValueError("Please specify a locator")
    if len(kwargs) > 1:
        raise ValueError("Please specify only one locator")
    k, v = next(iter(kwargs.items()))

    class Element(klass):
        locator = (_LOCATOR_MAP[k], v)

    return Element()


def multi_page_element(**kwargs):
    """ As for `page_element`, but returns a `MutliPageElement`
    """
    return page_element(klass=MultiPageElement, **kwargs)
