from setuptools import setup, find_packages

version = __import__('sendsms_admin').__version__

setup(
    name="django-sendsms-admin",
    version=version,
    url='http://github.com/stefanfoulis/django-sendsms-admin',
    license='BSD',
    platforms=['OS Independent'],
    description="A database delivery backend for django-sendsms (for debugging).",
    long_description=open('README.rst').read(),
    author='Stefan Foulis',
    author_email='stefan.foulis@gmail.com',
    maintainer='Stefan Foulis',
    maintainer_email='stefan.foulis@gmail.com',
    packages=find_packages(),
    install_requires=['django-sendsms',],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
