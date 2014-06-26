lottery
=======

This is a *very* basic running example for Pygrunn presentation on testing / monitoring. The presentation explains how to do testing & monitoring in the changing development environment where logic is moved from web server to browser client (javascript).

The lottery ticket site allows you to check whether you won a price on your ticket number. It checks if a ticket number is in the database. The datamodel consists of class Ticket with attribute number, and that's it.

This project is evolved in 3 simple steps:

- Pure Django. Setup Django, urls, views + template + forms (to check your ticket), admin (to enter data), tests (unittest and django_webtest)
- Start using javascript (ajax), with jquery + json view and very simple javascript string template. Test with Selenium and CasperJS
- Add Raven in Django and ravenjs to start monitoring exceptions and errors
