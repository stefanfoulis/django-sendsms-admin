====================
django-sendsms-admin
====================

A delivery backend for django-sendsms that delivers messages to the database instead of sending them. This is meant for
debugging. Also allows sending SMSs from the admin interface.

Installation
============

::

    pip install django-sendsms-admin

Then add ``sendsms_admin`` to ``INSTALLED_APPS`` and run ``syncdb`` or ``migrate``.
This already allows sending messages from admin. To enable the debug backend to
place all SMSs into the database::

    SENDSMS_BACKEND = 'sendsms_admin.backend.DatabaseSmsBackend'

