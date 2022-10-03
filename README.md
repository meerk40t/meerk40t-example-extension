# meerk40t-example-extension
MeerK40t example for dynamic extensions.

Extensions are more advanced plugins, but are generally not compatible with the Meerk40t version 0.7.x. These have a different entry_point and thus are not cross-loaded between versions.

# Secret Sauce - Entry_Points
Extensions in MeerK40t are used through entry_points, for an indepth explanation of these see: [https://amir.rachum.com/blog/2017/07/28/python-entry-points/]

The important part of this link is in `setup.cfg`.
```ini
[options.entry_points]
meerk40t.extension = Example = example.main:plugin
```

This tells meerk40t which looks for entry_points registered under `meerk40t.extension` that the `example` directory `main` script and `plugin` function will have our relevant code. You may have more than one entry.

If correctly registered and installed with `pip` meerk40t `plugin` command will add the relevant extensions to the internal extensions it already registers.
```
     ...
     kernel: example.main
     kernel: example.main
     Service Plugins:
     ...
     provider/device/lhystudios: example.main
     ...
     Module Plugins:
     module/wxMeerK40t: example.main
```

# Examples
The main.py example provides explanations of plugins and lifecycles and how to properly use the plugins

The examples are for a module plugin, a service plugin, a self-invaliding plugin, and a simple plugin.


# Simple MeerK40t plugin.

* Registers the console command: `example` which prints "Hello World".
* Registers a tree node option for: EngraveNode and CutNode which calls `example`.


# Installing

* Download into a directory:
* `$ pip install .`

# Development

* If you are developing your own extension for meerk40t you will want to use:
* `$ pip install -e .` this installs the python module in edit mode which allows you to easily see and experience your changes. Without reinstalling your module.
