FROM python:3

RUN pip install parallel-ssh

WORKDIR /usr/local/taf
COPY ./ /usr/local/taf

ENTRYPOINT ["python3"]
CMD ["boot_to_os.py"]