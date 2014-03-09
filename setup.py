from setuptools import setup, find_packages

requires = [ "requests>=2.1.0" ]

setup(name="green-etcd-client",
      version="0.1.0",
      platforms='any',
      packages = find_packages("etcd"),
      include_package_data=True,
      install_requires=requires,
      author = "Bogdan Gaza",
      author_email = "bc.gaza@gmail.com",
      url = "https://github.com/hurrycane/green-etcd-client",
      description = """Gevent powered etcd-client""",
      #entry_points = {'console_scripts': [ 'finny = finny.runner:execute_from_cli' ]},
      test_requirements = [],
      classifiers = [
        "Topic :: System :: Distributed Computing",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Topic :: Database :: Front-Ends",
      ]
)
