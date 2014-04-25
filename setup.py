from setuptools import setup

from uuid_upload_path import __version__


version_str = ".".join(str(n) for n in __version__)


setup(
    name = "django-uuid-upload-path",
    version = version_str,
    license = "BSD",
    description = "Generate short UUIDs and use them as paths for uploaded media files in Django.",
    author = "Dave Hall",
    author_email = "dave@etianen.com",
    url = "https://github.com/etianen/django-uuid-upload-path",
    packages = [
        "uuid_upload_path",
    ],
    test_suite = "uuid_upload_path.tests",
    zip_safe = True,
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
    ],
)
