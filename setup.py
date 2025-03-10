from setuptools import setup, find_packages

setup(
    name='sql_lib',
    version='0.1',
    packages=find_packages(include=['core*', 'tests*']),  # Явно включаем пакеты
    package_dir={'': '.'},
)