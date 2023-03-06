from nuclear import shell
from nuclear.sublog import log


def upgrade_trimmer_dependencies():
    log.info('Upgrading dependencies...')
    shell('pip3 install --upgrade --upgrade-strategy eager trimmer')
    log.info('Trimmer is up-to-date')
