FROM python:alpine as builder
RUN apk add --no-cache gcc build-base linux-headers
COPY ./netboot/requirements.txt .
RUN python3 -m pip install --user -r requirements.txt

FROM python:alpine
COPY --from=builder /root/.local /root/.local
RUN mkdir -p /opt/netboot
COPY . /opt/netboot
WORKDIR /opt/netboot
ENV PATH=/root/.local/bin:$PATH
EXPOSE 8000
CMD ["python3", "server.py"]
