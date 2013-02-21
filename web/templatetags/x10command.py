from django.template import Library
register = Library()


@register.filter
def cmd_line(cmd, dev):
    return cmd.cmd_line.format(dev.address)
