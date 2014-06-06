#!/usr/bin/env python3

# Examine a Plugin

import gi
gi.require_version("Gst", "1.0")
from gi.repository import Gst
Gst.init(None)


def main():
    print("Using Gst: {}.{}.{}.{}".format(*Gst.version()))

    registry = Gst.Registry.get()
    playback = registry.find_plugin("playback")

    if playback is not None:
        print("{}: {} {} {} {}".format(
            playback.get_name(),
            playback.get_version(),
            playback.get_source(),
            playback.get_package(),
            playback.get_version())
        )

        playbin = Gst.ElementFactory.make("playbin", None)

        # This utility function allows you to set properties
        # using the same syntax as gst-launch.
        Gst.util_set_object_arg(playbin, "flags", "video+buffering")

        print(playbin.get_property("flags"))


if __name__ == "__main__":
    main()
