"""Helper functions for testing."""
import glob


def return_test_files():
    """Return a list of all the *.raw files to run tests against."""
    platform_dirs = glob.glob('tests/*')

    platforms = []
    for platform in platform_dirs:
        platforms.append(glob.glob('%s/*' % platform))

    template_dirs = [item for sublist in platforms for item in sublist]

    test_commands = []
    for template_dir in template_dirs:
        test_commands.append(glob.glob('%s/*.raw' % template_dir))

    return [item for sublist in test_commands for item in sublist]
