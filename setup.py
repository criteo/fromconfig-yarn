"""Setup script."""

from pathlib import Path
import re
import setuptools


if __name__ == "__main__":
    # Read metadata from version.py
    with Path("fromconfig_yarn/version.py").open(encoding="utf-8") as file:
        metadata = dict(re.findall(r'__([a-z]+)__\s*=\s*"([^"]+)"', file.read()))

    # Read description from README
    with Path(Path(__file__).parent, "README.md").open(encoding="utf-8") as file:
        long_description = file.read()

    # Run setup
    setuptools.setup(
        author=metadata["author"],
        version=metadata["version"],
        classifiers=[
            "License :: OSI Approved :: Apache Software License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Intended Audience :: Developers",
        ],
        data_files=[(".", ["requirements.txt", "README.md"])],
        dependency_links=[],
        description=long_description.split("\n")[0],
        entry_points={"fromconfig0": ["yarn = fromconfig_yarn"]},
        install_requires=["fromconfig>=0.3.0", "skein", "cluster_pack"],
        long_description=long_description,
        long_description_content_type="text/markdown",
        name="fromconfig_yarn",
        packages=setuptools.find_packages(),
        tests_require=["pytest"],
        url="https://github.com/criteo/fromconfig-yarn",
    )
