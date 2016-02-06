###########
# IMPORTS #
###########

from colorclass import Color as colorize

#############
# FUNCTIONS #
#############

def success(string):
    return colorize("    ".join(["{higreen}[    OK    ]{/green}", string]))

def error(string):
    return colorize("    ".join(["{hired}[   FAIL   ]{/red}", string]))

def warning(string):
    return colorize("    ".join(["{hiyellow}[   WARN   ]{/yellow}", string]))

def title(string, color):
    return colorize("".join(["{", color, "}", string, "{/", color, "}"]))

def evidence(string, color):
    return colorize("".join(["{bg", color, "}{black}", string, "{/black}{/bg", color, "}"]))

def before_step(scheduler):
    return "\n".join(["",
                      "",
                      success("stepping")])

def after_step(scheduler):
    return str(scheduler())
