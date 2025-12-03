import logging
import struct
import time

import moderngl
import moderngl_window as mglw
from moderngl_window.conf import settings

import mglw_code.SETTINGS

"""
class RoleConf(mglw.WindowConfig):
    WINDOW = {
        "class": "moderngl_window.context.pygame2.Window",
        "gl_version": (3, 3),
        "title": "Role Engine",
        "size": (800, 600),
    }
"""

settings.WINDOW["class"] = "moderngl_window.context.pygame2.Window"
settings.WINDOW["title"] = "Role Engine"

wnd = mglw.create_window_from_settings()
ctx = moderngl.create_context()
mglw.activate_context(window=wnd, ctx=ctx)


class Run(mglw.WindowConfig):
    config = None
    window = None
    winConf = None
    timer = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Run.window = mglw.window
        Run.config = mglw.create_window_config_instance(self.__class__)
        Run.timer = Run.config.timer
        mglw.get_local_window_cls("pygame2")

    def Update():
        print(str(Run.timer))
        timer = Run.timer
        timer.start()

        while not wnd.is_closing:
            window = wnd
            current_time, delta = timer.next_frame()

            # Framerate  limit for hidden windows
            if not window.visible and Run.hidden_window_framerate_limit > 0:
                expected_delta_time = 1.0 / Run.hidden_window_framerate_limit
                sleep_time = expected_delta_time - delta
                if sleep_time > 0:
                    time.sleep(sleep_time)

            if Run.clear_color is not None:
                window.clear(*Run.clear_color)

            # Always bind the window framebuffer before calling render
            window.use()

            window.render(current_time, delta)

            if not window.is_closing:
                window.swap_buffers()

            _, duration = timer.stop()
            window.destroy()
            if duration > 0:
                mglw.logger.info(
                    "Duration: {0:.2f}s @ {1:.2f} FPS".format(
                        duration, timer.fps_average
                    )
                )

    def on_render(self, time: float, frametime: float):
        self.ctx.clear(0.1, 0.1, 0.1, 1.0)


def runWin():
    Run(ctx=ctx, wnd=wnd)
    Run.Update()
