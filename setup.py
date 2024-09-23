from setuptools import find_packages, setup

__version__ = "0.1.0"

setup(
    name="template_python",
    version=__version__,
    description="template for flask python application",
    author="Negar",
    python_requires=">=3.8.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "": ["*.yml"],
    },
    platforms=["Linux", "Mac OS"],
    zip_safe=False,
    install_requires=[
        # Add project dependencies here, for example:
        'gunicorn', 'Flask', 'requests',
    ]
)
