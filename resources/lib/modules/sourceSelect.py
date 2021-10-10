# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals

from resources.lib.database.skinManager import SkinManager
from resources.lib.modules.globals import g


def source_select(uncached_sources, source_list, item_information):
    selection = None

    try:
        if len(source_list) == 0:
            return None

        f = open("/storage/downloads/names.txt","w+")
        i = 0
        for n in source_list:
            i = i + 1
            n['counter'] = i
            f.write(n['release_title'] + "\n")

        f.close()

        from resources.lib.gui.windows.source_select import SourceSelect

        window = SourceSelect(
            *SkinManager().confirm_skin_path("source_select.xml"),
            item_information=item_information,
            sources=source_list,
            uncached=uncached_sources
        )

        selection = window.doModal()
        del window

        if selection is None:
            g.notification(g.ADDON_NAME, g.get_language_string(30032), time=5000)
            raise Exception
        if not selection:
            g.cancel_playback()

    finally:
        return selection
