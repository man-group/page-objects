Page Objects for Python
=======================

Page Objects are a testing pattern for websites. Page Objects model a page on
your site to provide accessors and methods for interacting with this page,
both to reduce boilerplate and provide a single place for element locators.

This project is an implementation of this pattern for Python using Selenium
webdriver. It is agnostic to test harnesses and designed to help you build up
libraries of code to test your sites.


.. image:: https://travis-ci.org/eeaston/page-objects.svg?branch=master
    :target: https://travis-ci.org/eeaston/page-objects


Documentation
-------------

https://page-objects.readthedocs.org


Quick Example
-------------

    >>> from page_objects import PageObject, PageElement
    >>> from selenium import webdriver
    >>>
    >>> class LoginPage(PageObject):
            username = PageElement(id_='username')
            password = PageElement(name='password')
            login = PageElement(css='input[type="submit"]')
    >>>
    >>> driver = webdriver.PhantomJS()
    >>> driver.root_uri = "http://example.com"
    >>> page = LoginPage(driver)
    >>> page.get("/login")
    >>> page.username = 'secret'
    >>> page.password = 'squirrel'
    >>> assert page.username.text == 'secret'
    >>> page.login.click()


Installation
------------

    $ pip install page_objects


Project History
---------------

This was originally part of the pkglib project at http://github.com/ahlmss/pkglib,
it has been forked to retain history.
