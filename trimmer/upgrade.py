from nuclear import shell
from nuclear.sublog import logger


def upgrade_trimmer_dependencies():
    logger.info('Upgrading dependencies...')
    shell('pip3 install --upgrade --upgrade-strategy eager trimmer')
    logger.info('Trimmer is up-to-date')
