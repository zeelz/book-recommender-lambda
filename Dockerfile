FROM public.ecr.aws/lambda/python:3.8.2023.12.06.11
# https://gallery.ecr.aws/lambda/python

COPY requirements.txt ${LAMBDA_TASK_ROOT}

RUN pip3 install -r requirements.txt

COPY data.py lambda_function.py processor.py ${LAMBDA_TASK_ROOT}/

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD ["lambda_function.lambda_handler"]