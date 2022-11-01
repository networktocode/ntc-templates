"""ntc_templates - Parse raw output from network devices and return structured data."""

try:
    from importlib import metadata
except ImportError:
    # Python version < 3.8
    import importlib_metadata as metadata

__version__ = metadata.version(__name__)
