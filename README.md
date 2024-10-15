# ExcGrouper

ExcGrouper is an intelligent exception grouping library that uses machine learning to automatically categorize and group similar exceptions without manual rules.

## Features

- 🤖 Automatic exception grouping using ML - no manual rules needed
- 🎯 Groups similar exceptions together based on semantic meaning
- 🔌 Easy integration with existing logging systems
- 🚀 Simple API for getting started quickly
- 🐳 Docker support for easy deployment

## Installation

```bash
pip install excgrouper
```

## Quick Start

### Docker Setup

To use ExcGrouper with Docker:

1. Clone the repository:
   ```
   git clone https://github.com/Owl-Sight-AI/excgrouper.git
   cd excgrouper
   ```

2. Build and start the Docker containers:
   ```
   docker-compose up -d
   ```

   This will start two containers:
   - ExcGrouper API server on port 8000
   - Qdrant vector database on port 6333

3. Install local dependencies

```bash
pip install -e .
```

4. You can now use the ExcGrouper API at `http://localhost:8000`
You can now use it with an example as `python examples/basic_usage.py`

### Basic Usage

```python
from excgrouper import ExcGrouper

grouper = ExcGrouper()

# Group an exception
group_id = grouper.group_exception("Connection refused to database xyz123", "ConnectionError")

# Get top exceptions
top_exceptions = grouper.get_top_exceptions(limit=10, days=1)
```

### Integrating with Existing Logger

You can easily integrate ExcGrouper with your existing logging setup:

```python
import logging
from excgrouper import ExcGrouper

# Set up ExcGrouper
grouper = ExcGrouper()

# Create a custom logging handler
class GroupingHandler(logging.Handler):
    def emit(self, record):
        if record.exc_info:
            exc_type, exc_value, _ = record.exc_info
            group_id = grouper.group_exception(str(exc_value), type_name=exc_type.__name__)
            record.msg = f"[Group: {group_id}] {record.msg}"

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
logger.addHandler(GroupingHandler())

# Now, when you log an error, it will be automatically grouped
try:
    1 / 0
except ZeroDivisionError as e:
    logger.error("An error occurred", exc_info=True)
```

For more detailed examples, check the `examples/` directory in the project repository.

## Documentation

For more detailed information, check out our [API Documentation](docs/API.md).

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.