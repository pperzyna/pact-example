# PACT Example Application

This is a python application for explanation of Contract Testing based on [Pact](https://docs.pact.io/).

## Getting Started

[![Build Status](https://travis-ci.org/pperzyna/pact-example.svg?branch=master)](https://travis-ci.org/pperzyna/pact-example)

### Prerequisites

What kind of things you need to install on your local computer to start:

* [Docker](https://www.docker.com/)
* [Docker-Compose](https://docs.docker.com/compose/)

### Installing

Run local stack via docker-compose
``` bash
docker-compose up --build
```

## Provider

This is a sample Flask application that expose endpoints with REST standard.

|  endpoint      | method   | payload | description |
| ---            | ---      | ---     | ---         |
| /user          | `GET`    | | show all users |
| /user          | `POST`   | `{'name','description'}` | create user |
| /user/**:id**  | `GET`    | | show user with **:id** |
| /user/**:id**  | `DELETE` | | delete user with **:id** |

## Consumer

This is a sample python script, which consume the information from provider. 

|  variable         | default               | description          |
| ---               | ---                   | ---                  |
| API_PROVIDER_URL  | http://localhost:5000 | URL of provider app  |

## Pact

Sample Contract (Pact): [consumer/src/pact/Consumer-Provider-pact.json](consumer/src/pact/Consumer-Provider-pact.json).

#### GENERATE

Run the tests on the consumer application. Check out the [entrypoint.sh](consumer/src/entrypoint.sh) file.

#### PUBLISH

``` bash
docker run -v $PWD/consumer/src/pact/:/usr/src/app/pact pactfoundation/pact-cli publish /usr/src/app/pact/ --consumer-app-version $GIT_COMMIT --tag=$GIT_BRANCH
```

#### VERIFY

``` bash
docker run pactfoundation/pact-cli verify --pact-broker-base-url=${PACT_BROKER_URL} --provider-base-url=${PROVIDER_URL} --provider-states-setup-url=${PROVIDER_URL}/_pact/provider_state --provider=Provider --provider-app-version=${GIT_COMMIT} --publish-verification-results --verbose
```

#### CAN-I-DEPLOY

``` bash
docker run pactfoundation/pact-cli broker can-i-deploy --broker-base-url=${PACT_BROKER_URL} -a Provider -e $GIT_COMMIT --to $GIT_BRANCH
```

#### CREATE-VERSION-TAG

``` bash
docker run pactfoundation/pact-cli broker create-version-tag -a Consumer -e $GIT_COMMIT -t $GIT_BRANCH
```