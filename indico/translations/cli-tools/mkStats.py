#!/usr/bin/env python3

import sys
import polib
from colors import color

po = dict()
for l in (["de_DE", "fr_FR", "pt_BR"]):
    po[l] = dict()
    for m in ("", "-js", "-react"):
        msg_file = "messages{0}.po".format(m)
        print("Reading {0} ({1})".format(msg_file, l), end=" ")
        p = polib.pofile(
                "indico/translations/{0}/LC_MESSAGES/{1}".format(
                    l, msg_file
                    )
                )
        if len(p.untranslated_entries()) == 0:
            print(len(p), color(len(p.untranslated_entries()), fg='green'))
        else:
            print(len(p), len(p.untranslated_entries()))
        po[l][msg_file]=p


po["en"] = dict()
for m in ("", "-js", "-react"):
    msg_file = "messages{0}".format(m)
    print("Reading {0} POT".format(msg_file), end=" ")
    p = polib.pofile(
            "indico/translations/{1}.pot".format(
                l, msg_file
                )
            )
    print(len(p))
    po["en"][msg_file]=p

