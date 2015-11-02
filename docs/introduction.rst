Introduction
============

Browser-based testing is hard to get right. There are wonderful tools out
there like Selenium that allow us to drive a web browser around our sites
with the minimum of effort to provide true integration tests.

With this great power however, comes a great way to create thousands of lines
of complicated test code with finicky timeouts and brittle execution. Tests
that are often easier to set fire to and re-write than fix when your designers
decide to change the layout of the HTML.

What Page Objects are for is to encourage you to write your browser tests
in a maintainable and supportable way that makes it easier to keep the
tests alive as the underlying site changes.

The Page Object model isn't new, or something that I've invented here.
There are numerous examples and discussions on the web:
http://lmgtfy.com/?q=Page+Object+Model

This is an implementation of the pattern for Python using Selenium webdriver
that I have found useful as my time as a developer. It is not tied to any
particular test framework. The codebase is tiny and has remained largely
unchanged for several years. I hope you enjoy using them as much as I have!
