from setuptools import setup

setup(
        name="ExploratoryDataAnalysis", 
        version="0.0.1",
        author="jjtena",
        author_email="josejustotena0@gmail.com>",
        description="Module for exporatory data analysis",
        long_description="Module with statistical and graphical methods to analyze a dataset",
        packages=['ExploratoryDataAnalysis'],
        install_requires=['matplotlib', 'seaborn', 'pandas', 'math'], 
        
        keywords=['python'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
        ]
)