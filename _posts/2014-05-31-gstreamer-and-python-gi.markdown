---
layout: post
title: "GStreamer and Python GI"
date: Sat 31 May 2014 05:15:28 PM CDT 
categories: gstreamer python
---

Let's take a brief look at how to get a Python-gi-based GStreamer program working. Here's the basic template:

{% highlight python3 %}
{% include gst-examples/example_1.py %}
{% endhighlight %}

You can run this puppy by saving it to a file and running:

{% highlight bash %}
$ python3 example_1.py
{% endhighlight %}

There's some fun stuff going on here, even if there's no pretty output.

{% highlight python %}
import gi
{% endhighlight %}

Firstly, we're importing the `gi` module, which is the GObject Introspection implementation for python. Suffice it to say that this is where the bindings for our GStreamer magic live -- you can always check out more about GObject and the Introspection support over at the GNOME project.

{% highlight python %}
gi.require_version("Gst", "1.0")
{% endhighlight %}

Then, we're requiring the version of "Gst" to be "1.0". Why? Because we want to target the latest and greatest GStreamer software, based on the 1.0 APIs, and if you happen to have the previous 0.10 software installed, the repository could inadvertently load it instead of the 1.0 libraries, and the 0.10 series does not play nice with the gobject introspection system.

{% highlight python %}
Gst.init(None)
{% endhighlight %}

Next, we're initalizing the GStreamer libraries.

Once we get inside `main()`, we're printing out the version of the GStreamer libraries that we're working with.

{% highlight python3 %}
print("Using Gst: {}.{}.{}.{}".format(*Gst.version()))
{% endhighlight %}

Finally, we're taking a look at the Registry, which is where GStreamer keeps track of all of the various plugins that provide functionality in the system. If you have need of a particular minimum version of a certain plugin, then you can use the Registry to make sure that your users have that version installed.

{% highlight python3 %}
registry = Gst.Registry.get()
plugins = registry.get_plugin_list()

for plugin in plugins:
    print("{}: {}".format(plugin.get_name(), plugin.get_version()))
{% endhighlight %}

[gstreamer]: http://gstreamer.freedesktop.org
[python]: http://www.python.org
