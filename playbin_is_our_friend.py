#!/usr/bin/env python3

# Playbin is our friend!

import gi
gi.require_version("Gst", "1.0")
from gi.repository import Gst
Gst.init(None)


class VideoPlayer(object):
    """The VideoPlayer object encapsulates a GStreamer pipeline and
    related callbacks to play an arbitrary video file using playbin."""

    def __init__(self):
        pass

    def _build_pipeline(self):

        # Pipelines are the fundamental "canvas" for GST
        self._pipeline = Gst.Pipeline()

        # The bus is the messaging layer
        self._bus = self._pipeline.get_bus()

        # We want to connect to messages on the bus
        self._bus.add_signal_watch()

        self.bus.connect('message::eos', self.on_eos)
        self.bus.connect('message::error', self.on_error)
        self.bus.connect('message::info', self.on_info)

        playbin = Gst.ElementFactory.make("playbin", None)

        # This utility function allows you to set properties
        # using the same syntax as gst-launch.
        # See:
        # http://lists.freedesktop.org/archives/gstreamer-devel/2012-December/038561.html
        Gst.util_set_object_arg(playbin, "flags", "video+buffering")


def check_installation():
    """Verify that VideoPlayer's dependencies are installed."""

    registry = Gst.Registry.get()
    playback = registry.find_plugin("playback")

    if playback is not None:
        print("Found {}: {} {} {} {}".format(
            playback.get_name(),
            playback.get_version(),
            playback.get_source(),
            playback.get_package(),
            playback.get_version())
        )
        return True
    else:
        return False


def main():
    print("Using Gst: {}.{}.{}.{}".format(*Gst.version()))

    if check_installation() is False:
        print("The playback plugin is not installed\
              -- please check your GStreamer installation.")


if __name__ == "__main__":
    main()
