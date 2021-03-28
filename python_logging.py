# config
import logging

logging_config = {
    'level': logging.DEBUG,
    'format': '%(levelname)s :: %(asctime)s :: %(name)s :: %(funcName)s :: %(lineno)s :: %(message)s',
    'datefmt': '%H:%M:%S'
}

# entry point
import logging

logging.basicConfig(**config.logging_config)

# usage
import logging

log = logging.getLogger(__name__)
