#include <pgmspace.h>

#define SECRET
#define THINGNAME "traffic_monitor"

const char WIFI_SSID[] = "Shivesh";
const char WIFI_PASSWORD[] = "shivu145@1";
const char AWS_IOT_ENDPOINT[] = "a2a3yhi4xeeldq-ats.iot.us-east-1.amazonaws.com";

// Amazon Root CA 1
static const char AWS_CERT_CA[] PROGMEM = R"EOF(
-----BEGIN CERTIFICATE-----
MIIDQTCCAimgAwIBAgITBmyfz5m/jAo54vB4ikPmljZbyjANBgkqhkiG9w0BAQsF
ADA5MQswCQYDVQQGEwJVUzEPMA0GA1UEChMGQW1hem9uMRkwFwYDVQQDExBBbWF6
b24gUm9vdCBDQSAxMB4XDTE1MDUyNjAwMDAwMFoXDTM4MDExNzAwMDAwMFowOTEL
MAkGA1UEBhMCVVMxDzANBgNVBAoTBkFtYXpvbjEZMBcGA1UEAxMQQW1hem9uIFJv
b3QgQ0EgMTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBALJ4gHHKeNXj
ca9HgFB0fW7Y14h29Jlo91ghYPl0hAEvrAIthtOgQ3pOsqTQNroBvo3bSMgHFzZM
9O6II8c+6zf1tRn4SWiw3te5djgdYZ6k/oI2peVKVuRF4fn9tBb6dNqcmzU5L/qw
IFAGbHrQgLKm+a/sRxmPUDgH3KKHOVj4utWp+UhnMJbulHheb4mjUcAwhmahRWa6
VOujw5H5SNz/0egwLX0tdHA114gk957EWW67c4cX8jJGKLhD+rcdqsq08p8kDi1L
93FcXmn/6pUCyziKrlA4b9v7LWIbxcceVOF34GfID5yHI9Y/QCB/IIDEgEw+OyQm
jgSubJrIqg0CAwEAAaNCMEAwDwYDVR0TAQH/BAUwAwEB/zAOBgNVHQ8BAf8EBAMC
AYYwHQYDVR0OBBYEFIQYzIU07LwMlJQuCFmcx7IQTgoIMA0GCSqGSIb3DQEBCwUA
A4IBAQCY8jdaQZChGsV2USggNiMOruYou6r4lK5IpDB/G/wkjUu0yKGX9rbxenDI
U5PMCCjjmCXPI6T53iHTfIUJrU6adTrCC2qJeHZERxhlbI1Bjjt/msv0tadQ1wUs
N+gDS63pYaACbvXy8MWy7Vu33PqUXHeeE6V/Uq2V8viTO96LXFvKWlJbYK8U90vv
o/ufQJVtMVT8QtPHRh8jrdkPSHCa2XV4cdFyQzR1bldZwgJcJmApzyMZFo6IQ6XU
5MsI+yMRQ+hDKXJioaldXgjUkK642M4UwtBV8ob2xJNDd2ZhwLnoQdeXeGADbkpy
rqXRfboQnoZsG4q5WTP468SQvvG5
-----END CERTIFICATE-----
)EOF";

// Device Certificate
static const char AWS_CERT_CRT[] PROGMEM = R"KEY(
-----BEGIN CERTIFICATE-----
MIIDWTCCAkGgAwIBAgIUJsNjAYrxEaqDSKU44FVC9DUVgtEwDQYJKoZIhvcNAQEL
BQAwTTFLMEkGA1UECwxCQW1hem9uIFdlYiBTZXJ2aWNlcyBPPUFtYXpvbi5jb20g
SW5jLiBMPVNlYXR0bGUgU1Q9V2FzaGluZ3RvbiBDPVVTMB4XDTIzMDUyODEyNDI0
OVoXDTQ5MTIzMTIzNTk1OVowHjEcMBoGA1UEAwwTQVdTIElvVCBDZXJ0aWZpY2F0
ZTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBANFa/2bcI7aNs7Wd0QQR
ZEzjWUXFo7HpZYXAMxe8BMtTfllRVxVLeP8uJLwnhvj5X9t3YbhsZ85M59NZ4uwH
Ix6inrT1p/2GYYiF3ANsBGv9txhL+1cgFWJNzOq3Qyz+By+jaMqtFP7A5nfvs6s/
h5s+PiBpfh1hL3MG7IPqpTXoxvY8dII/L+Hae1jiSvVz+lceWr1VEemwsccjhjVP
uZEXCXJ3RSgZztOzrtsXixXvVAfd2SXlAyICmIwbgTg6Jqf2NS5Ouuep/P1a4fII
21ZXujRPSvbYEXQJ4PRD/b6qrN2EQhNFJGrRmo8R2ZhKQj0GrSWt7I1RhTtqn9Fm
6rkCAwEAAaNgMF4wHwYDVR0jBBgwFoAU5gfwnMcjkiHGfxbV9LWQKdvbAXwwHQYD
VR0OBBYEFMnFDIeyfCeJLQ70Osz8vtaWqSYiMAwGA1UdEwEB/wQCMAAwDgYDVR0P
AQH/BAQDAgeAMA0GCSqGSIb3DQEBCwUAA4IBAQCsX3z5LpMTv/j/B4hUP0rgWO3m
m/DUR7sseptGn3IGbdrV+K++FNZAFZYB4qh/b7zAdz/N2ZgZA2UUsZEJjAPy11Ps
+cSqIzjM+uBAMITCl5vHuy1JPND/7Mk1IDDeBohzfzlrgrmYic/TqCa9QSE+AWht
5LH1BRTYL2Zm2AVhNhRzua5KdPpVT6Cn7qYibum07DMcE29k27/6CscLxVJj+W50
p4Oygm+aUGRq8YDDvW9Lc2c6E7sT8GDzHmVBqLbNCyYPuthXYInSXSsoSnnqd4ga
wT8nS0UA8wfnyb6EXm3xHa1qfKdzrLcaU0JUbMA4p3+beKTCJnT6BTfW/pMM
-----END CERTIFICATE-----
)KEY";

// Device Private Key
static const char AWS_CERT_PRIVATE[] PROGMEM = R"KEY(
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA0Vr/Ztwjto2ztZ3RBBFkTONZRcWjsellhcAzF7wEy1N+WVFX
FUt4/y4kvCeG+Plf23dhuGxnzkzn01ni7AcjHqKetPWn/YZhiIXcA2wEa/23GEv7
VyAVYk3M6rdDLP4HL6Noyq0U/sDmd++zqz+Hmz4+IGl+HWEvcwbsg+qlNejG9jx0
gj8v4dp7WOJK9XP6Vx5avVUR6bCxxyOGNU+5kRcJcndFKBnO07Ou2xeLFe9UB93Z
JeUDIgKYjBuBODomp/Y1Lk6656n8/Vrh8gjbVle6NE9K9tgRdAng9EP9vqqs3YRC
E0UkatGajxHZmEpCPQatJa3sjVGFO2qf0WbquQIDAQABAoIBAC2Nk00aUVsDcjru
X/B2qFBil6Yq3vdzRXfY3kUn0BM905wzqrMjfOxpaezW3POHr2fdjhHG5L9q1HaU
dF/PHcEouUe+vBLaDpbaKYlFE6E7z38l6UaH4J9HNnNL9P3xODcRY1fWWV8lMgCe
04VLiYIqBPKggaR65QwuUYBSqigUXR6RAkpGZ5PHrsHfjB9Ko07GsIQ2ZVKrY4vl
qHaEyP5BJqpARrzCTjbBirwVqxP8bJYz6O7yFDUe/H3j+ud7FId64qM8RUXreT+7
b5Dx4uhQ1+Yi3vFyaG412X0jOP4y/W+LsOLSxoRg/1osLoMayNUnNMWPXD5wsUyf
HR6/yZECgYEA/wI2FgOU9nkCs203EZOLyKC56Qkr6lFky0vq4iUmM2lFq9wawxRd
zwpOtWUlTH+3QhuZn88CuRJqZTuSsZFVyTW88Jn9R0OdXfcob0BaCdTYgb02smmL
62SjZuuqj+dfKRZWoK/EGoO8nbyHEkerPcPHoeixi8iChfAgX2Yb3ocCgYEA0ita
AvNqELntx+SEstUu4TBcRUYGXxWXQqAcDegkXM+GmHtO6x2Ns1zSvnnjd4B4Qdgm
p3GK/ATEDATpKjaL97fjohvXgq5yv7YwczCdljlC5Z2boOBI4jB2o6EcAwj8vx5o
AOvynequYIIyJ1Yy8hdw/RP6+zK7U4C1bny5/L8CgYARJN7p//el0mDiGzeWkOrW
5CdbiWhQaoRyPnpeFc1Jq4wpj7Sk5Nuhrbm47EHjsLprUVu0qMAwHRLWF3k3QuQX
kOtQ6aljfyI3TQSE5jinbI3ZuxTQTdRAURXDN5jR7+Yv5vaP+wEeHzkxCZmzGupi
TqU/N1uoYCSWSJyEjWLWRQKBgBiaapcd17TNj0BvR/mHa02BU8voPqay6FosVBxs
qJUU1jTTepGbjBMLMsCJlE9RAsLygtPnPtXx2OFvUbxXVltRc5xulfP+aAB5W4Kg
llIXsfUfVjCnEOEpuzm8ioLwcmYNMS+qb2R9LJyvoR9pv90HUXrO8/qkHbnQv2yH
vV4RAoGBAJhcG2kSMH0ngjie1+Xeq2wVY4ZMsLt2kPSG7Bt/MOoRjOTS97IkYykW
vG9ApdAVNkn/2nNL0exkGT0SuwNHqmDBqFq5Y97ZEj5q/QPpBJ9RtDskf1SIRO1m
K4LrGhUer3PSYxkoQ6Ybf1rLG3G5jTCT7qNGLJ1vxcQYZ8hQuY19
-----END RSA PRIVATE KEY-----
)KEY";