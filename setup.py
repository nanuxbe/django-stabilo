from setuptools import setup, find_packages

version = '0.1'

setup(
    name='django-stabilo',
    version=version,
    description="Text highlighting features.",
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='django',
    author='Baptiste Mispelon',
    author_email='bm@m2bpo.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
