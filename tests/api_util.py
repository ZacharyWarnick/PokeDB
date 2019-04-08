import os

from coverage import Coverage
from io import StringIO
from pathlib import Path
from unittest import TextTestRunner, TestLoader


_TEST_DIR = Path(__file__).parent
_IDB_DIR = _TEST_DIR.parent / 'idb'
_OUTPUT_DIR = _TEST_DIR / 'cover'
_OUT_PREFIX = 'cover_'
_OUT_SUFFIX = '.log'


def _log_file(unique_name: str):
    """Creates a correctly patterned log file name.

    Args:
        unique_name: The identifier that is formatted into the general pattern.

    Returns:
        A string value for the file name, including the extension.
    """
    return '{pre}{name}{suf}'.format(
        pre=_OUT_PREFIX,
        name=unique_name,
        suf=_OUT_SUFFIX)


def _is_log(fpath: Path):
    """Determines if a file path is a testing result log file.

    Note:
        This specifically checks for a pattern match in accordance with the
        format prescribed by `_log_file(unique_name)`.

    Args:
        fpath: The path object to a file that needs to be checked.

    Returns:
        True if the path points to a log file, otherwise False.
    """
    return (fpath.is_file()
            and fpath.stem.startswith(_OUT_PREFIX)
            and (fpath.suffix == _OUT_SUFFIX))


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
    return _OUTPUT_DIR / _log_file(version)


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


def _prepare_dir(out_file: Path):
    """Creates the output directory and deletes old logs (if needed)."""
    out_file.parent.mkdir(parents=True, exist_ok=True)

    for f in out_file.parent.iterdir():
        # Delete old log files to save space.
        if (f.name != out_file.name) and _is_log(f):
            f.unlink()


def get_coverage_result(label=None):
    """Obtains the results of running coverage for all unit tests.

    Args:
        label: A string or integer which uniquely identifies a test result.

    Returns:
        A string containing testing results and a code coverage report.
    """
    out_file = _get_output_file(label)
    if not out_file.exists():
        _prepare_dir(out_file)
        output = _run_coverage()

        with out_file.open(mode='w+') as f:
            f.write(output)

        return output
    else:
        with out_file.open() as f:
            return f.read()
