import os

from coverage import Coverage
from io import StringIO
from pathlib import Path
from unittest import TextTestRunner, TestLoader


_TEST_DIR = Path(__file__).parent
_IDB_DIR = _TEST_DIR.parent / 'idb'
_OUTPUT_DIR = _TEST_DIR / 'cover'


def _get_target_files():
    """Globs python test files located in this directory.

    Note:
        Each test file must be named like 'test*.py' to be included.

    Returns:
        A list of python module names as strings.
    """
    test_files = list(_TEST_DIR.glob('test*.py'))
    source_files = list(_IDB_DIR.glob('*.py'))

    # We don't want to generate coverage for `__init__.py`.
    def not_init(x): return '__init__' != x.stem
    source_files = list(filter(not_init, source_files))

    return list(map(str, test_files + source_files))


def _get_output_file(default='default'):
    """Creates a file path to use for saving the testing/coverage results.

    This file name generated is always set to be located in a folder called
    'cover' that is adjacent to this file (i.e. in the 'tests' folder). This
    allows for multiple files to be created without having to include specific
    .gitignore rules for each file.

    Note:
        This method checks for a GAE_VERSION environment variable to use as the
        name for the coverage file. This will allow the app to cache a version
        specific coverage result, removing the need to re-run coverage every
        time an API request is made.

    Note:
        This does not create the 'cover' directory automatically. The directory
        should be created just before coverage is actually run.

    Args:
        default (optional): The file name (without the extension) that should
            be used when the GAE_VERSION environment variable isn't present.
            The default value is 'default'.

    Returns:
        A path object for the location where results should be saved.
    """
    version = os.environ.get('GAE_VERSION', default)
    return _OUTPUT_DIR / '{}.out'.format(version)


def _run_coverage():
    targets = _get_target_files()
    test_out = StringIO()
    loader = TestLoader()
    runner = TextTestRunner(test_out)
    test_suite = loader.discover(_TEST_DIR)

    # Run coverage on test suites.
    cov = Coverage(
        branch=True,
        include=targets,
        omit=[],
        config_file=False)
    cov.start()
    runner.run(test_suite)
    cov.stop()

    cov_out = StringIO()
    cov.report(file=cov_out, show_missing=True)

    return '{}\n{}'.format(test_out.getvalue(), cov_out.getvalue())


def get_coverage_result(label=None):
    out_file = _get_output_file(label)
    if not out_file.exists():
        out_file.parent.mkdir(parents=True, exist_ok=True)
        output = _run_coverage()

        with out_file.open(mode='w+') as f:
            f.write(output)

        return output
    else:
        with out_file.open() as f:
            return f.read()
