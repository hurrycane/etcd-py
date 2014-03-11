from setuptools import setup, find_packages

requires = [ "requests>=2.1.0", "grequests>=0.2.0" ]

setup(name="py-etcd",
      version="0.1.1",
      platforms='any',
      packages = find_packages(),
      include_package_data=True,
      install_requires=requires,
      author = "Bogdan Gaza",
      author_email = "bc.gaza@gmail.com",
      url = "https://github.com/hurrycane/etcd-py",
      description = """Full fledged etcd-client for python. Gevent-ready. Batteries included""",
      keywords = ['etcd', 'client', 'gevent', 'greenlet', 'green', 'etcd-clien'],
      #entry_points = {'console_scripts': [ 'finny = finny.runner:execute_from_cli' ]},
      test_requirements = [],
      classifiers = [
        "Topic :: System :: Distributed Computing",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Topic :: Database :: Front-Ends",
      ]
)
