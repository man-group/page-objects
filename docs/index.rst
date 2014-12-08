Page Objects for Python
=======================


Page Objects are a testing pattern for websites. Page Objects model a page on
your site to provide accessors and methods for interacting with this page,
both to reduce boilerplate and provide a single place for element locators.

This project is an implementation of this pattern for Python using Selenium
webdriver. It is agnostic to test harnesses and designed to help you build up
libraries of code to test your sites.

The Python Selenium API is documented here: http://selenium-python.readthedocs.org


Quick Example
-------------

.. code-block:: pycon

    >>> from page_objects import PageObject, PageElement
    >>> from selenium import webdriver
    >>>
    >>> class LoginPage(PageObject):
            username = PageElement(id_='username')
            password = PageElement(name='password')
            login = PageElement(css='input[type="submit"]')

    >>> driver = webdriver.PhantomJS()
    >>> driver.get("http://example.com")
    >>> page = LoginPage(driver)
    >>> page.username = 'secret'
    >>> page.password = 'squirrel'
    >>> assert page.username.text == 'secret'
    >>> page.login.click()


Installation
------------

.. code-block:: bash

    $ pip install page_objects


Table Of Contents
=================

.. toctree::

      introduction
      tutorial
      best_practices
      history

* :ref:`genindex`
* :ref:`modindex`
