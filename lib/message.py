LEVEL_NOTE = 0
LEVEL_INFO =1
LEVEL_WARNING = 2
LEVEL_HOLE = 3
LEVEL_STOP=4
def debug(fmt, *args):
    print(fmt % args)
def _problem(level, body):
    debug('[LOG] <%s> %s', ['note', 'info', 'warning', 'hole','stop'][level], body)

security_note = lambda body : _problem(LEVEL_NOTE, body)
security_info = lambda body : _problem(LEVEL_INFO, body)
security_warning = lambda body : _problem(LEVEL_WARNING, body)
security_hole = lambda body : _problem(LEVEL_HOLE, body)
security_stop=lambda body : _problem(LEVEL_STOP, body)