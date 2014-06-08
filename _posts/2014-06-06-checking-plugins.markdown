---
layout: post
title: "Checking Plugins"
date: "Fri Jun 06 06:26:13 -0500 2014"
---
GStreamer is a plugin-based system, so while it's extremely flexible, it also has complexity around which elements & features are available to use on a particular installation.

Luckily, it also has some nice features to help cope with the complexity. Our next example shows how to verify that a plugin is installed, as well as get some information about it.

{% highlight python3 %}
{% include gst-examples/examine_plugin.py %}
{% endhighlight %}

For our example, we use the 'playback' plugin, which contains one of the most useful built-in elements for Gstreamer: _playbin_.

We'll talk more about playbin next.
