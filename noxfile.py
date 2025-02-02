# type: ignore
import nox


PYTHON_VERSION = '3.8'
PY_PATHS = ['django_clienthints', 'tests', 'noxfile.py']

REQUIREMENTS_FORMAT = ['black==20.8b1', 'isort==5.6.4', 'docformatter==1.3.1']
REQUIREMENTS_LINT = [*REQUIREMENTS_FORMAT, 'flake8==3.8.4']

nox.options.reuse_existing_virtualenvs = True
nox.options.sessions = ['lint']


@nox.session(name='format', python=PYTHON_VERSION)
def format_(session):
    """Format the code."""
    session.install(*REQUIREMENTS_FORMAT)
    session.run(
        'black', '-l', '88', '-t', 'py38', '-S', '--exclude=.*/migrations/.*', *PY_PATHS
    )
    session.run('isort', *PY_PATHS)
    session.run(
        'docformatter',
        '--in-place',
        '--recursive',
        '--wrap-summaries=88',
        '--wrap-descriptions=88',
        *PY_PATHS,
    )


@nox.session(python=PYTHON_VERSION)
def lint(session):
    """Run linters."""
    session.install('-e', '.', *REQUIREMENTS_LINT)
    session.run(
        'black',
        '-l',
        '88',
        '-t',
        'py38',
        '-S',
        '--exclude=.*/migrations/.*',
        '--check',
        *PY_PATHS,
    )
    session.run('isort', '--check', *PY_PATHS)
    session.run(
        'docformatter',
        '--check',
        '--recursive',
        '--wrap-summaries=88',
        '--wrap-descriptions=88',
        *PY_PATHS,
    )
    session.run('flake8', *PY_PATHS)
