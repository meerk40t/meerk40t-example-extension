
def module_plugin(module, lifecycle):
    """
    This example plugin attaches to the module/wxMeerK40t for the opening and closing of the gui. If the gui is never
    launched this plugin is never activated. wxMeerK40t is the gui wx.App object. If the module is loaded several times
    each module will call this function with the specific `module`

    :param module: Specific module this lifecycle event is for.
    :param lifecycle: lifecycle event being regarded.
    :return:
    """
    print(f"module:example {lifecycle}")
    if lifecycle == 'module':
        # Responding to "module" makes this a module plugin for the specific module replied.
        return "module/wxMeerK40t"
    elif lifecycle == 'module_open':
        print("wxMeerK40t App was lauched.")
    elif lifecycle == 'module_close':
        print("wxMeerK40t App was closed.")
    elif lifecycle == 'shutdown':
        print("wxMeerK40t App shutdown.")


def service_plugin(service, lifecycle):
    """
    This example plugin attaches to the lihuiyu device service. Every lihuiyu device will have each lifecycle event
    passed to this plugin. There may be more than one such driver.

    :param service:
    :param lifecycle:
    :return:
    """
    print(f"service:example {lifecycle}")
    if lifecycle == "service":
        # Responding to "service" makes this a service plugin for the specific services created via the provider
        return "provider/device/lhystudios"
    elif lifecycle == 'added':
        """
        Service is added to the list of services for this provider type. In our example we are checking the device
        services for any lihuiyu devices. This occurs when ever the provider is used to create this service type.
        """
        print(f"A lihuiyu device was added: {service}")
    elif lifecycle == 'service_attach':
        """
        Our given service is attached. The current context.device is the 'service' passed in this plugin. Only one
        service maybe attached at any particular time. So our current device is the passed service.
        """
        print(f"A lihuiyu device was attached: {service}")
    elif lifecycle == 'assigned':
        """
        This is a plugin was started flagged to be assigned. For many drivers this launches their respective config
        window. This will usually happen if our driver was created in devices. It's triggered by setting the `assigned`
        flag as true during activation.
        """
        print(f"A lihuiyu device assigned: {service}")
    elif lifecycle == 'service_detach':
        """
        Our given service is no longer the context.device for the kernel. This will happen if a different device is
        being attached or all services are being shutdown.
        """
        print(f"A lihuiyu device was detached: {service}")
    elif lifecycle == 'shutdown':
        """
        The service is shutdown. This occurs if the service is removed or if the entire kernel is being shutdown.
        """
        print(f"A lihuiyu device was shutdown: {service.name}")


def invalidating_plugin(kernel, lifecycle):
    if lifecycle == "precli":
        kernel.register("invalidating_plugin_existed", True)
    if lifecycle == "invalidate":
        return True


def simple_plugin(kernel, lifecycle):
    """
    Simple plugin. Catches the lifecycle it needs registers some values.

    @param kernel:
    @param lifecycle:
    @return:
    """
    if lifecycle == "register":
        # Example command extension to the console commands. Type: "example" in console, and this code will work.
        @kernel.console_command('example', help="Says Hello World.")
        def example_cmd(command, channel, _, **kwargs):
            """
            Example is part of the meerk40t example plugin this command only prints hello world. This part of the
            command will show up in the extended help for "help example".
            """
            channel(_('Hello World'))

        # Example tree extension for Cut and Engrave nodes to call our Hello World function.
        @kernel.elements.tree_operation("Hello World", node_type=("op cut", "op engrave"), help="calls `example` code.")
        def unique_tree_name_example(node, **kwargs):
            """
            This adds this command to the right-click tree. Any cut or engrave node type will include "Hello World".
            :param node:
            :param kwargs:
            :return:
            """
            kernel.console("example\n")


def plugin(kernel, lifecycle):
    """
    This is our main plugin. It provides examples of every lifecycle event and what they do and are used for. Many of
    these events are simply to make sure some module events occur after or before other module events. The lifecycles
    also permit listeners to attach and detach during the lifecycle of a module, and insures everything can interact
    smoothly.

    :param kernel:
    :param lifecycle:
    :return:
    """
    print(f"Kernel plugin calling lifecycle: {lifecycle}")
    if lifecycle == "plugins":
        """
        All plugins including ones added with this call are added to the kernel. A list of additions plugins will add
        those to the list of plugins.
        """
        return [service_plugin, module_plugin, invalidating_plugin, simple_plugin]
    if lifecycle == "service":
        """
        Responding to this with a service provider makes this plugin a service plugin.
        
        Note: Normally we ignore this lifecycle.
        """
        return None  # This is not a service plugin, check service_plugin for an example of that.
    if lifecycle == "module":
        """
        Responding to a registered module provider makes this plugin a module plugin.
        
        Note: Normally we ignore this lifecycle.
        """
        return None  # This is not a module plugin, check module_plugin for an example of this.
    if lifecycle == "precli":
        """
        This lifecycle occurs before the command line options are processed. Anything part of the main CLI is processed
        after this.
        """
    if lifecycle == "cli":
        """
        This life cycle is intended to process command line information. It is sometimes used to register features or
        other flags that could be used during the invalidate.
        """
        if kernel.lookup("invalidating_plugin_existed"):
            print("Our invalidating plugin existed and put this here.")
    if lifecycle == "invalidate":
        """
        Invalidate is called with a "True" response if this plugin isn't valid or cannot otherwise execute. This is
        often useful if a plugin is only valid for a particular OS. For example `winsleep` serve no purpose for other
        operating systems, so it invalidates itself.
        """
        return False  # We are valid.

    if lifecycle == 'preregister':
        """
        During the pre-register phase the module wxMeerK40t is registered and opened in gui mode.
        """
        pass
    if lifecycle == 'register':
        """
        Register our various processes. These should modify the registered values within meerk40t. This stage is
        used for general purpose lookup registrations.
        """
        # See simple plugin for examples of registered objects.
        pass

    if lifecycle == 'configure':
        """
        Configure is a preboot stage where everything is registered but elements are not yet booted.
        """
        pass
    elif lifecycle == 'boot':
        """
        Start all services.
        
        The kernel strictly registers the lookup_listeners and signal_listeners during this stage. This permits modules
        and services to listen for signals and lookup changes during the active phases of their lifecycles.  
        """
        pass
    elif lifecycle == 'postboot':
        """
        Registers some additional choices such as some general preferences.
        """
    elif lifecycle == 'prestart':
        """
        CLI specified input file is loading during the pre-start phase.
        """
        pass
    elif lifecycle == 'start':
        """
        Nothing happens.
        """
        pass
    elif lifecycle == 'poststart':
        """
        Nothing happens.
        """
        pass
    elif lifecycle == 'ready':
        """
        Nothing happens.
        """
        pass
    elif lifecycle == 'finished':
        """
        Nothing happens.
        """
        pass
    elif lifecycle == 'premain':
        """
        Nothing happens.
        """
        pass
    elif lifecycle == 'mainloop':
        """
        This is the start of the gui and will capture the default thread as gui thread. If we are writing a new gui
        system and we need this thread to do our work. It should be captured here. This is the main work of the program.
        
        You cannot ensure that more than one plugin can catch the mainloop. Capture of the mainloop happens for the
        duration of the gui app, if one exists. 
        """
        pass
    elif lifecycle == 'postmain':
        """
        Everything that was to grab the mainloop thread has finished. We are fully booted. However in most cases since
        the gui has been killed, the kernel has likely been told to shutdown too and will end shortly.
        """
        pass
    elif lifecycle == 'preshutdown':
        """
        Preshutdown saves the current activated device to the kernel.root to ensure it has the correct last value.
        """
        pass

    elif lifecycle == 'shutdown':
        """
        Meerk40t's closing down. Our plugin should adjust accordingly. All registered meerk40t processes will be stopped
        any plugin processes should also be stopped so the program can close correctly. Depending on the order of
        operations some operations might not be possible at this stage since the kernel will be in a partially shutdown
        stage.
        """
        pass
