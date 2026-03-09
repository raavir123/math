# use official python image
FROM python:3.9

# set working directory
WORKDIR /app

# code copy
COPY calculator .

# command to run app
CMD ["python", calculator.py"]