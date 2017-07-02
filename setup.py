from setuptools import setup, find_packages

setup(
        name="MOYA-player",
        version="0.1",
        packages=find_packages(),
        author="Nikolay Babulkov",
        author_email="nbabulkov@gmail.com",
        description="Simplistic music player",
        license="MIT",
        url="https://github.com/nbabulkov/moya-player",
        keywords="player music mp3 audio",
        packages=["player"]
)


