from cliglue.utils.shell import shell


def upgrade():
    shell('pip3 install --upgrade youtube-dl')
