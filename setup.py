from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="excgrouper",
    version="0.1.0",
    author="Owl-Sight-AI",
    author_email="ai.observability.eng@gmail.com",
    description="Automatic exception grouping using AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Owl-Sight-AI/ExcGrouper",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[git init
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.7",
    install_requires=[
        "docker-compose",
        "fastapi",
        "openai",
        "qdrant-client",
        "requests",
        "sentence-transformers",
        "uvicorn",
    ],
    extras_require={
        "dev": ["pytest", "black", "isort"],
    },
)