# ftmcloud Task Queue Worker

## Overview
The ```ftmcloud``` Task Queue Worker application is a Celery-based application designed to trigger bulk data processing and
ingestion tasks. In general, this application serves as the consumer/subscriber end of a pub-sub architecture.

## Structure

### core
Contains logic relating to the core application functionality as well as logic that is crosscutting.

### tasks
Contains domain-specific task logic that can be executed at any point in time. These are separated by type of task
and further by domain.

## Application Logic
Tasks are defined in an object-oriented pattern in which each desired task should inherit from the "BaseTask" class. In
general, tasks should subscribe to independent queues each with their own separate priorities and maximum number of
concurrent tasks.

### TODO:
* Define BaseTask abstraction structure and queue-based subscription system
* Document edge cases that may result in concurrency concerns (i.e. deadlock)
* Document types of tasks
* Develop pipeline system for defining sub-tasks where necessary
* Develop error system and functionality to log errors to file
* Boost test coverage for all tasks
* Setup CI/CD to run tests
* Abstract some of the MongoDB functionality to incorporate transactions and write concerns (see https://www.mongodb.com/docs/manual/core/transactions/)