import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yt-transcript",
    version="0.0.1",
    author="Marc Levine",
    author_email="levinems@3sys.com",
    description="this is a simple package to grab youtube transcripts when allowed by video author",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="youtube-api subtitles youtube transcripts transcript subtitle youtube-subtitles youtube-transcripts cli",
    url="https://github.com/levinems/yt-transcript",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)