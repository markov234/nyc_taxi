# Uses Python 3.9 image as base.
FROM python:3.9

# Installs pandas and other libraries inside the container.
RUN pip install pandas sqlalchemy requests psycopg2 pyarrow

# Sets the working directory inside the container to /app. Where pipeline.py below will be copied to in the container.
WORKDIR /app
# Copies my pipeline.py file (first one) to the container as pipeline.py (second one).
COPY ingest_data.py ingest_data.py

# Opens 'bash' shell when container starts instead of default python shell.
# ENTRYPOINT [ "bash" ]

# Opens python shell and runs pipeline.py when container starts.
ENTRYPOINT [ "python", "ingest_data.py" ]