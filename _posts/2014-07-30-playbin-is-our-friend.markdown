---
layout: post
title: "Playbin Is Our Friend"
date: "Wed Jul 30 06:55:47 -0500 2014"
---

As the title says, Gstreamer's `playbin` element is a versatile, easy-to-use, jack-of-all trades way to build a pipeline without needing to know much at all up front.

You may be wondering what you would need to know up front -- it's a media file, right? You just play it! Well, here are just a few things you need to know in order to handle playback of a media file in a way users will enjoy:

* Is it audio? Video? Both?
* What is the format of the media? Is it raw PCM data(a WAV file)? Compressed video? Is it MPEG-2, MPEG-4? Windows Media Video (aka VC1)?
* What is the container format? For various reasons, media content gets stored in files with metadata called containers -- you can store MP4 video using a QuickTime container, or you could take the same data and put it into a Matroska container. Different players understand different containers.
* What are the metadata tags in the video?
* Once the media is decompressed, what format is the 'raw' media? Is it 8-bit audio? HD video? 44.1 kHz? 

There are plenty more, but these are the kinds of things that a player needs to be able to figure out and then handle. The beautiful thing about playbin is that it takes advantage of the features of GStreamer to handle all of these things for you.


