FROM golang:1.16-alpine

WORKDIR /goapp

COPY go.mod ./
COPY go.sum ./
RUN go mod download

COPY . ./

RUN go build -o /goserver

EXPOSE 5000

CMD [ "/goserver" ]
