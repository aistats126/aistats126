import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nshap",
    version="0.0.1",
    description="Python package to compute n-Shapley Values.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=["nshap"],
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "matplotlib",
        "seaborn",
        "xgboost",
        "folktables",
        "scikit-learn",
        "interpret",
        "pandas",
        "shap",
        "jupyterlab",
    ],
)
