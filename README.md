# summer-practice-task
Here is an app which allows to create configuration files for SoC simulators.

## app/
### Files contains:
- *app_core.py*: here is main core module which provides structure to contain simulator classes, their attributes and
methods; also here is an Extractor class with converting to .json and writing to file methods.
- *app_widgets*: set of classes with QWidget parent: here is objects with necessary fields and methods for
reading information from them. Check for validity is also provided.

> You should edit this files firstly to add fields or to change their functionality

## config/
### Files contains
- *style_settings*: contains style sheet for main window and other elements with width parameters.

## main.py

This is the main script with main window structure. Start this file to run the application.

> If you want to make an experiment with style, the arrangement of elements, their display and properties, you should
> edit structure of this file.


Nick Proshak,
Copyright (c) 2023, MIT licence,
HSE summer practice task.
