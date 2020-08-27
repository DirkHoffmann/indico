.. _install-dev:

Translations
************

Indico comes with a number of languages by default. In release 2.3, those are: 
English (default), French, Portuguese, Spanish and Chinese (in the order of integration).
Additional languages are being prepared on the Transifex platform.

In order to use (partially) existing translations from Transifex or to contribute 
translations, you need to register with the
`Indico project on the Transifex platform <https://www.transifex.com/indico/>`_.

Additional Translations
=======================

This is a guide 
(courtesy `pedrovsky <https://talk.getindico.io/t/including-a-new-language-in-indico/1864/5>`_) 
to set up an Indico instance with a new language. 
It is useful for translators when applying their revisions to verify how the translation looks in production
or for administrators who just want to lurk at the incubated translation embryos.

Create your own Indico instance
-------------------------------

This could be in our own computer, in a shared machine or even your organisation, if the latter gives you permission.

For creating your own Indico instance, we provide two different guides:
The first one is for a `production system <../installation/production>`_, 
it will prepare Indico to be served to users and used in all the different purposes you may have besides translations. 
The second is `development <../installation/development>`_ a light-weight, 
easier to set up, version oriented to testing purposes, that should not be exposed to the public.

However, for the purpose of translation **development** or **testing** which are the purpose of this guide, 
we recommend and only provide the steps when using the development version.

Installing the `transifex client <https://docs.transifex.com/client/installing-the-client>`_
--------------------------------------------------------------------------------------------

Get an API token
----------------

Go `here <https://www.transifex.com/user/settings/api/>`_ and generate your API token. 
Afterwards, you should run the command ``tx init --skipsetup``. 
It will request the token you just copied from the previous settings and save it locally so you can start using transifex locally.
If you do not know how to run this command, 
please refer to the guide `here <https://docs.transifex.com/client/init>`_.

Install the translations
------------------------

Navigate to the src folder inside Indico path.

Run ``tx pull -f -l <language_code>``. 
Languages codes can be obtained `here <https://www.transifex.com/indico/indico/dashboard/>`_. 
For example, Chinese (China) is zh_CN.GB2312.

Compile and Run Indico
----------------------

Run the commands ``indico i18n compile-catalog`` 
and ``indico i18n compile-catalog-react`` 
and `launch Indico <../installation/development/#running-indico>`_. 
The language should now show up as an option in the top right corner.

FAQ
---

Why isn’t Indico loading my language?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some languages in transifex use codes that Indico is not able to recognise.
One example is the Chinese’s zh_CN.GB2312.
The easy fix to this is to rename the folder in ``indico/translations/zh_CN.GB2312`` 
to ``zh_Hant_TW``. 
Unfortunately, there isn’t any list with mappings for all the languages. 
So if by any reason it doesn’t work for you, feel free to `ask us <../contact>`_.


Contributing
************

