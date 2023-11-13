from setuptools import setup


setup(
    name='cldfbench_dplace-dataset-ea',
    py_modules=['cldfbench_dplace-dataset-ea'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'dplace-dataset-ea=cldfbench_dplace-dataset-ea:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
