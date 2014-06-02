#!/usr/bin/env python3
# Example 1

import gi
gi.require_version("Gst", "1.0")
from gi.repository import Gst
Gst.init(None)


def main():
    print("Using Gst: {}.{}.{}.{}".format(*Gst.version()))

    registry = Gst.Registry.get()
    plugins = registry.get_plugin_list()

    for plugin in plugins:
        print("{}: {}".format(plugin.get_name(), plugin.get_version()))

if __name__ == "__main__":
    main()
