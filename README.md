Page Objects for Python
=======================

Page Objects are a testing pattern for websites. Page Objects model a page on
your site and provide accessors and methods for interacting with this page,
both to reduce boilerplate and provide a single place for element locators.

This project is an implementation of this pattern for Python using Selenium
webdriver.

[![Build Status](https://travis-ci.org/eeaston/page-objects.svg?branch=master)](https://travis-ci.org/eeaston/page-objects)



Documentation
-------------

https://page-objects.readthedocs.org


Quick Example
-------------

    >>> from page_objects import PageObject, page_element
    >>> from selenium import webdriver
    >>>
    >>> class LoginPage(PageObject):
            username = page_element(id_='username')
            password = page_element(name='password')
            login = page_element(css='input[type="submit"]')

    >>> driver = webdriver.PhantomJS()
    >>> driver.get("http://example.com")
    >>> page = LoginPage(driver)
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
